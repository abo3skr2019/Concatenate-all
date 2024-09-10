import os
import glob

def concatenate_markdown_files(directory):
    # Find all markdown files in the directory and subdirectories
    markdown_files = glob.glob(os.path.join(directory, '**', '*.md'), recursive=True)
    
    # Open the output file in write mode
    with open('concatenated.md', 'w', encoding='utf-8') as outfile:
        for md_file in markdown_files:
            # Write the file name as a header
            outfile.write(f'Filename = {os.path.basename(md_file)}\n\n')
            with open(md_file, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write('\n\n')  # Add a newline between files for separation

# Example usage
if __name__ == '__main__':
    concatenate_markdown_files(os.getcwd())