import os
import glob
import re
import argparse

def concatenate_markdown_files(directory, ignore_tags=False, include_filenames=True, use_relative_path=False):
    """
    Concatenates all markdown files in the specified directory into a single file.

    Parameters:
    directory (str): The directory to search for markdown files.
    ignore_tags (bool): Whether to ignore lines with tags.
    include_filenames (bool): Whether to include filenames as headers.
    use_relative_path (bool): Whether to use relative paths for filenames.
    """
    try:
        # Find all markdown files in the directory and subdirectories
        markdown_files = glob.glob(os.path.join(directory, '**', '*.md'), recursive=True)
        
        # Open the output file in write mode
        with open('concatenated.md', 'w', encoding='utf-8') as outfile:
            for md_file in markdown_files:
                if include_filenames:
                    # Write the file name as a header
                    if use_relative_path:
                        filename = os.path.relpath(md_file, directory).replace(os.sep, '\\\\')
                    else:
                        filename = os.path.basename(md_file)
                    outfile.write(f'# Filename = {filename}\n\n')
                with open(md_file, 'r', encoding='utf-8') as infile:
                    inside_tag_block = False
                    for line in infile:
                        if ignore_tags:
                            if re.match(r'^---\s*$', line.strip()):
                                inside_tag_block = not inside_tag_block
                                continue
                            if inside_tag_block:
                                continue
                        outfile.write(line)
                    outfile.write('\n\n')  # Add a newline between files for separation
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description='Concatenate all markdown files in a directory.')
    parser.add_argument('directory', type=str, help='The directory to search for markdown files.')
    parser.add_argument('--ignore-tags', action='store_true', help='Ignore lines with tags.')
    parser.add_argument('--include-filenames', action='store_true', help='Include filenames as headers.')
    parser.add_argument('--use-relative-path', action='store_true', help='Use relative paths for filenames.')
    
    args = parser.parse_args()
    
    concatenate_markdown_files(args.directory, args.ignore_tags, args.include_filenames, args.use_relative_path)

if __name__ == '__main__':
    main()