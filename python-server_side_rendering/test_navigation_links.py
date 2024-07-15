import requests

def test_navigation_links():
    response = requests.get('http://127.0.0.1:5000')
    assert response.status_code == 200, "Failed: Home page did not load successfully"
    content = response.text
    assert '<a href="/">Home</a>' in content, "Failed: Home link not found in navigation"
    assert '<a href="/about">About</a>' in content, "Failed: About link not found in navigation"
    assert '<a href="/contact">Contact</a>' in content, "Failed: Contact link not found in navigation"
    print("All navigation links are present and correct.")

if __name__ == "__main__":
    test_navigation_links()
