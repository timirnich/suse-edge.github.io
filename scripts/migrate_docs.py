import re
import subprocess
import sys
import argparse
from pathlib import Path

def is_git_repo(path: Path) -> bool:
    try:
        subprocess.run(['git', 'status'], cwd=path, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def main():
    parser = argparse.ArgumentParser(description="Migrate AsciiDoc files based on migration_plan.md")
    parser.add_argument("--dry-run", action="store_true", help="Print what would happen without making any changes")
    args = parser.parse_args()

    root_dir = Path.cwd()
    migration_plan_path = root_dir / 'asciidoc' / 'migration_plan.md'
    
    if not migration_plan_path.exists():
        print(f"Error: {migration_plan_path} not found.")
        sys.exit(1)
        
    git_repo = is_git_repo(root_dir)
    print(f"Git repository detected: {git_repo}")
    if args.dry_run:
        print("--- DRY RUN MODE: No files will be moved ---")
    
    with open(migration_plan_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    # Find the table
    table_lines = [line for line in lines if line.strip().startswith('|')]
    if len(table_lines) < 3:
        print("Error: Could not find a valid markdown table.")
        sys.exit(1)
        
    # Skip header and separator
    data_lines = table_lines[2:]
    
    # Build a map of all .adoc files in asciidoc/ to their paths for fuzzy finding
    asciidoc_dir = root_dir / 'asciidoc'
    all_adocs = list(asciidoc_dir.rglob('*.adoc'))
    adoc_map = {p.name: p for p in all_adocs}
    
    moved_sources = set()
    
    for line in data_lines:
        parts = [p.strip() for p in line.split('|')]
        if len(parts) < 4:
            continue
            
        source_raw = parts[1]
        target_raw = parts[2]
        
        if not source_raw or source_raw.startswith('N/A'):
            continue
            
        # Extract just the filename (e.g., "atip-quickstart.adoc (Topologies snippet)" -> "atip-quickstart.adoc")
        match = re.search(r'([\w\./-]+\.adoc)', source_raw)
        if not match:
            print(f"Warning: Could not parse source filename from '{source_raw}'. Skipping.")
            continue
            
        source_name = match.group(1)
        target_path = asciidoc_dir / target_raw
        
        # Try to find the source file
        source_file = None
        
        # 1. Exact path relative to root or asciidoc
        if (root_dir / source_name).exists():
            source_file = root_dir / source_name
        elif (asciidoc_dir / source_name).exists():
            source_file = asciidoc_dir / source_name
        else:
            # 2. Try replacing the first dash with a slash (e.g., components-rancher.adoc -> components/rancher.adoc)
            slash_name = source_name.replace('-', '/', 1)
            if (asciidoc_dir / slash_name).exists():
                source_file = asciidoc_dir / slash_name
            else:
                # 3. Try to find by name in the rglob map
                if source_name in adoc_map:
                    source_file = adoc_map[source_name]
                else:
                    # 4. Try finding by splitting the dash (e.g. components-fleet.adoc -> fleet.adoc)
                    base_name = source_name.split('-')[-1]
                    if base_name in adoc_map:
                        source_file = adoc_map[base_name]

        if not source_file:
            # Maybe it was already moved?
            for moved_src, moved_tgt in moved_sources:
                if source_name in str(moved_src):
                    source_file = moved_tgt
                    print(f"Source file {moved_src.relative_to(root_dir)} was already moved to {moved_tgt.relative_to(root_dir)}. Will copy from there.")
                    break
            
            if not source_file:
                print(f"LOG: Cannot find source file for '{source_raw}' (searched for '{source_name}')")
                continue
        
        if source_file == target_path:
            continue
            
        is_copy = False
        for moved_src, moved_tgt in moved_sources:
            if source_file == moved_tgt:
                is_copy = True
                break
                
        print(f"{'Copying' if is_copy else 'Moving'}: {source_file.relative_to(root_dir)} -> {target_path.relative_to(root_dir)}")
        
        if not args.dry_run:
            # Ensure target directories exist
            target_path.parent.mkdir(parents=True, exist_ok=True)
            
            if is_copy:
                import shutil
                shutil.copy2(source_file, target_path)
                print(f"  Copied because source was already moved to multiple targets.")
            else:
                if git_repo:
                    try:
                        subprocess.run(['git', 'mv', str(source_file), str(target_path)], check=True)
                    except subprocess.CalledProcessError as e:
                        print(f"Error moving {source_file} with git mv: {e}")
                else:
                    source_file.rename(target_path)
                moved_sources.add((source_file, target_path))
        else:
            if not is_copy:
                moved_sources.add((source_file, target_path))

if __name__ == '__main__':
    main()
