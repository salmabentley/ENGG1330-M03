import os
import sys
import textwrap
import re

# --- ANSI Styling Codes ---
BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
BRIGHT_WHITE = "\033[97m"
RESET = "\033[0m"
REVERSE = "\033[7m"

def process_markdown_paragraph(paragraph):
    """
    1. Parses markdown syntax and wraps the *plain text* first (no ANSI codes yet).
    2. Applies ANSI styling to the cleanly wrapped lines afterward.
    """
    paragraph = paragraph.rstrip()
    
    # 1. Headers (#, ##, ###)
    if paragraph.startswith("# "):
        text = paragraph[2:].upper()
        return [f"{BOLD}{CYAN} {text} {RESET}"]
    elif paragraph.startswith("## "):
        return [f"{BOLD}{YELLOW}▶ {paragraph[3:]}{RESET}"]
    elif paragraph.startswith("### "):
        return [f"{BOLD}{BRIGHT_WHITE}• {paragraph[4:]}{RESET}"]
        
    # 2. Blockquotes (> )
    if paragraph.startswith("> "):
        clean_text = paragraph[2:]
        wrapped_q = textwrap.wrap(clean_text, width=72)
        return [f"{DIM}  │ {line}{RESET}" for line in wrapped_q]
        
    # 3. Bullet points (* or -)
    if paragraph.startswith("* ") or paragraph.startswith("- "):
        clean_text = paragraph[2:]
        wrapped_b = textwrap.wrap(clean_text, width=74)
        styled_lines = []
        for i, line in enumerate(wrapped_b):
            prefix = " • " if i == 0 else "   "
            styled_lines.append(f"{prefix}{line}")
        return styled_lines

    # 4. Standard Paragraphs: Wrap plain text FIRST, then apply inline styles
    wrapped_plain = textwrap.wrap(paragraph, width=76)
    styled_paragraph_lines = []
    
    for line in wrapped_plain:
        # Apply inline bold (**text**) safely after wrapping
        styled_line = re.sub(r'\*\*(.*?)\*\*', f'{BOLD}{BRIGHT_WHITE}\\1{RESET}', line)
        styled_paragraph_lines.append(f"  {styled_line}")
        
    return styled_paragraph_lines

def display_md(filepath):
    """Reads a .md file, applies styles, wraps to 76 cols, and pages within 24 rows."""
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    # Step 1: Wrap and style paragraphs while preserving layout structure
    wrapped_lines = []
    for paragraph in raw_text.splitlines():
        if not paragraph.strip():
            wrapped_lines.append("") # Keep empty line breaks
        else:
            processed_lines = process_markdown_paragraph(paragraph)
            wrapped_lines.extend(processed_lines)

    # Step 2: Chunk into pages of 18 lines max to strictly respect 24-row limits
    lines_per_page = 18
    pages = [wrapped_lines[i:i + lines_per_page] for i in range(0, len(wrapped_lines), lines_per_page)]
    if not pages:
        pages = [[]]

    current_page = 0
    total_pages = len(pages)

    while True:
        # Clear screen and move cursor to top-left corner
        sys.stdout.write("\033[H\033[J")

        # Rows 3–20: Render up to 18 lines
        page_content = pages[current_page]
        for line in page_content:
            sys.stdout.write(f"  {line:<76}  \n")
            
        # Fill remaining empty rows to lock the screen layout steady
        for _ in range(lines_per_page - len(page_content)):
            sys.stdout.write(" " * 80 + "\n")

        # Row 21: Divider line
        sys.stdout.write("─" * 80 + "\n")
        
        # Row 22: Footer status info
        status = f" Page {current_page + 1} of {total_pages} "
        sys.stdout.write(f"{BOLD}{status:<80}{RESET}\n")
        
        # Row 23: Navigation instructions
        sys.stdout.write("[N]ext Page  |  [P]revious Page  |  [E]xit Document\n")
        
        # Row 24: Input prompt locked strictly to the bottom row
        cmd = input("> ").strip().lower()

        if cmd == 'n' and current_page < total_pages - 1:
            current_page += 1
        elif cmd == 'p' and current_page > 0:
            current_page -= 1
        elif cmd in ['e', 'q', 'exit']:
            break

