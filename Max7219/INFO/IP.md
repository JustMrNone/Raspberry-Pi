An IP address (Internet Protocol address) is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication. It serves two primary functions: identifying the host or network interface and providing the location of the device in the network. Here's a breakdown of the structure:

### Types of IP Addresses

1.  **IPv4 (Internet Protocol version 4)**:

    -   **Format**: An IPv4 address consists of four octets (or bytes), each ranging from 0 to 255, separated by dots. For example: `192.168.1.1`.
    -   **Structure**: Each octet is an 8-bit binary number, making a total of 32 bits (4 bytes).
    -   **Example**:
        -   `192.168.1.1`
        -   Binary: `11000000.10101000.00000001.00000001`
    -   **Address Classes**: IPv4 addresses are divided into classes (A, B, C, D, E) based on the leading bits:
        -   **Class A**: `0xxxxxxx` (1.0.0.0 to 127.255.255.255) - Used for very large networks.
        -   **Class B**: `10xxxxxx` (128.0.0.0 to 191.255.255.255) - Used for medium-sized networks.
        -   **Class C**: `110xxxxx` (192.0.0.0 to 223.255.255.255) - Used for small networks.
        -   **Class D**: `1110xxxx` - Reserved for multicast groups.
        -   **Class E**: `1111xxxx` - Reserved for experimental purposes.
2.  **IPv6 (Internet Protocol version 6)**:

    -   **Format**: An IPv6 address consists of eight groups of four hexadecimal digits, separated by colons. For example: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`.
    -   **Structure**: Each group represents 16 bits, making a total of 128 bits (16 bytes).
    -   **Example**:
        -   `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
        -   Simplified: `2001:db8:85a3::8a2e:370:7334` (using the double colon to represent consecutive groups of zeros).
    -   **Address Types**:
        -   **Global Unicast**: Publicly routable addresses.
        -   **Link-Local**: Used for communication within a local network segment (starts with `fe80::`).
        -   **Multicast**: Used to send packets to multiple destinations.

### Components of an IPv4 Address

1.  **Network Part**:

    -   The portion of the IP address that identifies the specific network. The length of this part can vary based on the subnet mask.
    -   For example, in `192.168.1.1` with a subnet mask of `255.255.255.0`, the network part is `192.168.1`.
2.  **Host Part**:

    -   The portion of the IP address that identifies a specific device within that network.
    -   In the example above, `1` is the host part, identifying a specific device within the `192.168.1.x` network.
3.  **Subnet Mask**:

    -   Determines how the IP address is divided into the network and host parts.
    -   Written in decimal (like `255.255.255.0`) or CIDR notation (like `/24`, which indicates that the first 24 bits are the network part).

### Summary

-   **IPv4**: 32 bits divided into 4 octets (e.g., `192.168.1.1`).
-   **IPv6**: 128 bits divided into 8 groups of hexadecimal digits (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).
-   Each IP address contains a **network part** and a **host part**, determined by the subnet mask.

This structure allows devices to communicate over the Internet and on local networks effectively.