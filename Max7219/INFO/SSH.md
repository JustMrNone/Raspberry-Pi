Here's a streamlined summary based on the methods that worked for setting up a static IP connection between your Raspberry Pi and Windows PC over Ethernet:

* * * * *

### On the Raspberry Pi

1.  **Assign a Static IP Using NetworkManager**:
    -   First, confirm the connection name (`"Wired connection 1"` for your Ethernet).

    -   Run the following commands to set up the static IP:

        bash

        Copy code

        `sudo nmcli con modify "Wired connection 1" ipv4.addresses "192.168.2.2/24"
        sudo nmcli con modify "Wired connection 1" ipv4.gateway "192.168.2.1"
        sudo nmcli con modify "Wired connection 1" ipv4.dns "192.168.2.1"
        sudo nmcli con modify "Wired connection 1" ipv4.method manual
        sudo nmcli con up "Wired connection 1"`

    -   This will set the Raspberry Pi's Ethernet IP to `192.168.2.2`, with the gateway and DNS pointing to `192.168.2.1`.

### On Windows

1.  **Configure Static IP**:

    -   Go to **Control Panel > Network and Sharing Center > Change adapter settings**.
    -   Right-click the Ethernet connection used for the Raspberry Pi and select **Properties**.
    -   Select **Internet Protocol Version 4 (TCP/IPv4)**, then click **Properties**.
    -   Set:
        -   **IP address**: `192.168.2.1`
        -   **Subnet mask**: `255.255.255.0`
        -   **Default gateway**: Leave blank.
2.  **Test the Connection**:

    -   Open Command Prompt on Windows and ping the Raspberry Pi to confirm the connection:

        cmd

        Copy code

        `ping 192.168.2.2`

3.  **SSH Access**:

    -   Use the following command to SSH into the Raspberry Pi from Windows:

        bash

        Copy code

        `ssh pi@192.168.2.2`

* * * * *

This setup ensures a stable, static connection over Ethernet with your Raspberry Pi reachable at `192.168.2.2` and your Windows PC at `192.168.2.1`.