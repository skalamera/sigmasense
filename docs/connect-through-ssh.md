# Connect through SSH

# Connect through SSH

Sigma supports connecting through Secure Shell (SSH) for [PostgreSQL](/docs/connect-to-postgresql), [Redshift](/docs/connect-to-redshift), [AlloyDB](/docs/connect-to-alloydb), and [MySQL](/docs/connect-to-mysql) connections.

The SSH protocol is a secure remote shell protocol, where clients and servers communicate on a secure channel. It has three layers:

|  |  |
| --- | --- |
| **Transport layer** | Secures communication between the server and the client, monitors data encryption and decryption, protects the integrity of the connection, caches data, and performs data compression. |
| **Authentication layer** | Performs client authentication at the beginning of each session. |
| **Connection layer** | Manages communication channels after successful authentication. |

SSH channels use public key cryptography to authenticate the client. After establishing the connection, SSH encrypts information to safely exchange it between the server and the client. This provides the data security that is independent of the particular network infrastructure.

## Requirements

* Admin privileges in your Sigma organization; see [account types](/docs/user-account-types).
* A PostgreSQL, Redshift, AlloyDB or MySQL database.

## SSH server parameters

To enable SSH connections, send the following Sigma information to your system admin.

|  |  |
| --- | --- |
| **Public key** | [Download](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/downloads/ssh-public-key.txt)     ``` ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCfBoABeXmQjlx+Sc8V3WWMMPQKtFUEeRhg64WrZ0Om922TpJum1967LzGkHP/RIdZa95S0m8WRbGOzl9TeSzUz3jz2/NOxfwzzv/UKGsytzrkWaUZICPK/HlHF7kYWAT6gxMP3MGALwepYWwtPBAk+R3tba+T7siZYjI0URY+uFg329CiRuilPZ3AtsPoXQqEH3sdTPfT6RUKytiVSwCZgwsnzp4LyE2lSGTKRvMm90S+k5rPeQ20N9A6LAtLrFjCpaOwEqPK7JFJqAamOcST7mI/lYsB7+f6BuH8I7Vq+1xdHFEQ1Uy1KelxLcwdJ5FAsjdGPWb1pKYZInXfd/CxnFMyr++PVYOz6xCAxpfWzCn6zCYUieqsjUPk5mYxz4+tc7ejuWUTHf/htiPfW2JwUObt8xo0y4xIJ8G4qzueovlz5BxWyA55OfjOOqNU7OsyRMvqkSQrfvWtfD3T8RrL82fOUewGFur3RJYD1/Nj9RX8cZDjDipxStarFO1ORBDWwSzNPHkn/xzNWc/IsSPKsN9ZATFkUIN1PXjCqqhVhIrLCFb63DLK9xjo3JdQ40oYjHN1YCKLF5E2f+kjz4jZZSjvN+uDDp2BjV5a75bQvZjXOB32gjNnjZdi6krZEh9z//3NKj55zwqynjn0JTq3/dgQFYItVP4F4/bJORBcUfQ== [email protected] ``` |
| **User** | sigmacomputing |
| **Sigma IP addresses** | Sigma's egress IP addresses are listed on all individual connection pages in the Sigma **Administration** portal. |

## Get Sigma IPs

Follow these steps to get Sigma IPs from the app:

1. Open your Admin Portal to the **Connection** page.
2. Select any connection, or click **Create Connection**.
3. Look for the IP addresses under connection credentials.

## Connect to Sigma through SSH

1. Download or save Sigma’s [SSH public key](https://sigma-docs-screenshots.s3.us-west-2.amazonaws.com/downloads/ssh-public-key.txt).
2. Add Sigma IPs to your allowlist.
3. Create an SSH **user account**, and name it *sigmacomputing*.  
   The user *sigmacomputing* authenticates through the public key.
4. Authorize Sigma's public key according to the instructions of your SSH server.
5. For most servers, the SSH default **port** is 22. It is also the default port on Sigma.  
   Check that the **port** on your SSH server matches the port on Sigma.
6. In Sigma, navigate to your connection’s page in the **Admin Portal**.
   1. Under **Connection Credentials**, switch on the **SSH Tunnel**.
      Set these parameters:

      |  |  |
      | --- | --- |
      | **Tunnel host** | This is your IP address. |
      | **Tunnel port** | This value must match the port of your SSH server.  Sigma's defaults to port 22, which is common for most servers. |

      ![SSH tunnel configuration](https://files.readme.io/9c7e113-connection-ssh.png)
7. If you are editing an existing connection, click **Save**.  
   If you are creating a new connection, continue specifying the **Connection features**, **Write access**, and so on.

Updated 3 days ago

---

Related resources

* [Connect to PostgreSQL](/docs/connect-to-postgresql)
* [Connect to Redshift](/docs/connect-to-redshift)
* [Connect to AlloyDB](/docs/connect-to-alloydb)
* [Connect to MySQL](/docs/connect-to-mysql)

* [Table of Contents](#)
* + [Requirements](#requirements)
  + [SSH server parameters](#ssh-server-parameters)
  + [Get Sigma IPs](#get-sigma-ips)
  + [Connect to Sigma through SSH](#connect-to-sigma-through-ssh)