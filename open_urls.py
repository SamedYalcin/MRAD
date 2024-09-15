import webbrowser

# Path to your text file
file_path = r""

# Open URLs
def open_urls(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
    
    for url in urls:
        url = url.strip()  # Remove any leading/trailing whitespace
        if url:  # Check if the URL is not empty
            webbrowser.get('windows-default').open_new(url)  # Open URL in default browser

# Run the function
open_urls(file_path)
