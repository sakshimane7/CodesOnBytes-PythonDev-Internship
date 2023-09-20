import re


def is_valid_ipv4(ip):
    # Regular expression to match IPv4 address
    ipv4_pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'

    # Check if the format matches
    match = re.match(ipv4_pattern, ip)
    if not match:
        return False

    # Check each octet for validity (0-255)
    for octet in match.groups():
        if int(octet) > 255:
            return False

    return True


# Example usage
ip_address = "192.168.0.1"
if is_valid_ipv4(ip_address):
    print(f"{ip_address} is a valid IPv4 address")
else:
    print(f"{ip_address} is not a valid IPv4 address")
