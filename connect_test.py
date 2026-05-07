import requests
import urllib3

# Suppress the InsecureRequestWarning from verify=False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def test_vcenter_connection(ip):
    try:
        response = requests.get(
            f"https://{ip}/rest/com/vmware/cis/session",
            verify=False,
            timeout=10  # Avoid hanging indefinitely
        )
        is_online = response.status_code == 401
        print(f"Lab Status: {'Online' if is_online else f'Offline (unexpected status: {response.status_code})'}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not reach the host — check IP or network")
    except requests.exceptions.Timeout:
        print("Error: Request timed out")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_vcenter_connection("192.168.1.100")  # Replace with your 1800X lab IP
