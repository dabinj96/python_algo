import requests
from bs4 import BeautifulSoup

def decode_secret_message(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Error downloading the document.")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    grid_entries = []
    
    # try to find a table in the HTML.
    table = soup.find("table")
    if table:
        rows = table.find_all("tr")
        for row in rows:
            # Look for table cells; 
            cells = row.find_all(["td", "th"])
            if len(cells) == 3:
                # Extract the text from each cell.
                cell_texts = [cell.get_text(strip=True) for cell in cells]
                try:
                    x = int(cell_texts[0]) 
                    ch = cell_texts[1]
                    y = int(cell_texts[2])
                    grid_entries.append((x, y, ch))
                except ValueError:
                    continue    
                
    if not grid_entries:
        print("No valid grid entries were found.")
        return

    # Determine grid dimensions.
    max_x = max(x for x, y, ch in grid_entries)
    max_y = max(y for x, y, ch in grid_entries)

    # Create a grid filled with spaces (assuming (0,0) is the top-left).
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y, ch in grid_entries:
        grid[y][x] = ch

    # Print the grid row by row.
    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
    decode_secret_message(url)