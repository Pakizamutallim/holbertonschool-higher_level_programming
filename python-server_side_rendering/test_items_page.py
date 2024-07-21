import requests

def test_items_page():
    base_url = 'http://127.0.0.1:5000'
    response = requests.get(f'{base_url}/items')
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert "Items List" in response.text, "Items List header not found"
    assert "<li>Python Book</li>" in response.text, "Python Book not found in items list"
    assert "<li>Flask Mug</li>" in response.text, "Flask Mug not found in items list"
    assert "<li>Jinja Sticker</li>" in response.text, "Jinja Sticker not found in items list"

if __name__ == '__main__':
    test_items_page()
