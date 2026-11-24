# Mission 07 — Computer Networks

## 1. Task / objective
The goal of this mission is to understand foundational computer networking concepts:
1. Define and compare fundamental networking terms (LAN, MAN, WAN, DNS, Router, Protocol, Packet Switching, and Client-Server architecture).
2. Execute macOS-compatible network diagnostic commands (`dig` and `ping`) against a public example domain (`example.com`).
3. Analyze what each network test reveals and clarify their diagnostic limitations.
4. Detail the step-by-step lifecycle of what happens when a web browser requests and displays a webpage, correctly using core networking terminology.

---

## 2. Work completed

### Task 7.1 — Network Concepts Table

| Concept | Meaning and Core Purpose | Real-World Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | High-speed network connecting devices within a small, localized geographic footprint (single room, home, or university lab). | Wi-Fi network connecting laptops and printers inside my college computer laboratory. |
| **MAN (Metropolitan Area Network)** | Network spanning a larger metropolitan area or city-wide organization. | City municipal Wi-Fi network or regional cable television network connecting branches across a city. |
| **WAN (Wide Area Network)** | Network spanning broad geographical boundaries (states, countries, continents) interconnecting multiple smaller networks. | The global Internet connecting universities, data centers, and internet service providers worldwide. |
| **DNS (Domain Name System)** | Hierarchical naming system translating human-readable domain names into machine-routable numerical IP addresses. | Translating `example.com` into IP address `172.66.147.243`. |
| **Router** | Layer-3 networking device that inspects packet destination IP addresses and forwards data across separate networks using routing tables. | Home Wi-Fi gateway forwarding packets from local private subnets to the Internet Service Provider (ISP). |
| **Protocol** | Standardized set of rules and message formats governing how devices communicate, format, transmit, and receive digital data. | HTTP/HTTPS (web content transfer), TCP (reliable connection), IP (addressing and routing). |
| **Packet Switching** | Networking paradigm where messages are partitioned into small discrete packets transmitted independently across shared paths and reassembled at the destination. | Streaming music or loading web pages: packets travel across different Internet nodes and reassemble in correct order. |
| **Client-Server Architecture** | Distributed computing model where client applications request data or services and centralized servers process requests and return responses. | Web browser (client) requesting a web page from an Apache/Nginx web server hosting the website. |

---

### Task 7.2 — Practical Network Diagnostics

Diagnostic commands were executed against public domain `example.com`:

#### 1. DNS Resolution Test (`dig example.com`)
```bash
dig example.com
```
- **Observations:**
  - Status: `NOERROR` (resolution successful).
  - Queried Domain: `example.com. IN A`
  - Returned IP Addresses (A Records): `172.66.147.243` and `104.20.23.154`.
  - DNS Resolver Server: `8.8.8.8#53` (Google Public DNS).
  - Response Time: 39 milliseconds.
- **What this test establishes:** Confirms that local and upstream DNS recursive resolvers are functional and can successfully resolve the domain name into an active IPv4 address.
- **What this test cannot establish:** It does not prove that the destination server is physically powered on, accepting network traffic, or running a responsive web application.

#### 2. Network Reachability and Latency Test (`ping -c 3 example.com`)
```bash
ping -c 3 example.com
```
- **Observations:**
  - Sent 3 ICMP echo requests of 56 data bytes each.
  - Received 3 replies with 64 bytes each (`ttl=58`).
  - Packet loss: `0.0% packet loss`.
  - Latency: `min = 5.662 ms`, `avg = 22.699 ms`, `max = 45.276 ms`.
- **What this test establishes:** Proves end-to-end IP network connectivity between my local computer and the destination host at Layer 3 (Network Layer) and measures round-trip latency.
- **What this test cannot establish:** It does not verify whether application ports (such as HTTP port 80 or HTTPS port 443) are open, nor does it confirm whether the web server daemon is functioning properly (many cloud hosts reply to ICMP pings even when the web server is offline).

---

### Task 7.3 — Step-by-Step Lifecycle: Opening a Website

When a user opens a web browser and navigates to a website (e.g., `https://example.com`), the following sequence occurs:

1. **User Initiation (Client):** The user enters a URL into the web browser (the **Client**). The browser first checks its local cache and the operating system's DNS resolver cache to see if the corresponding IP address was recently looked up.
2. **Domain Name Resolution (DNS):** If not cached, the client sends a query to the configured **DNS** server. The recursive resolver queries root, top-level domain (.com), and authoritative nameservers until it resolves `example.com` into its IP address (`172.66.147.243`).
3. **Packet Transmission & Routing (Router):** The client encapsulates the HTTP request into IP data packets and forwards them to the local default gateway (**Router**). Intermediate routers throughout the Internet examine the packet headers and route them hop-by-hop toward the destination.
4. **Transport Layer Handshake (Protocol):** The client and destination server establish a reliable connection using the TCP/IP **Protocol** via a 3-way handshake (`SYN` $\rightarrow$ `SYN-ACK` $\rightarrow$ `ACK`), followed by a TLS cryptographic handshake to establish encrypted HTTPS communication.
5. **Sending the HTTP Request:** The client sends an HTTP GET request packet over the secure channel specifying the requested resource (e.g., `GET / HTTP/1.1`).
6. **Processing at the Destination (Server):** The remote web **Server** receives and decodes the request, processes the application logic, and prepares an HTTP **Response** containing a status code (`200 OK`) and the webpage payload (HTML, CSS, assets).
7. **Receiving Response & Rendering:** The server transmits response packets back through the network **Routers** to the client. The browser reassembles the packets, parses the HTML, executes JavaScript, and paints the webpage visuals on the display screen.

---

## 3. Commands / tools used
- `dig`: Queried DNS servers to inspect A records and DNS lookup timing.
- `ping`: Tested ICMP network reachability, packet loss, and round-trip times.

## 4. My understanding
- DNS functions as the Internet's address book: humans remember intuitive names (`example.com`), but network hardware relies on numerical IP addresses (`172.66.147.243`) to route packets.
- `ping` and `dig` test completely different layers of the networking stack: `dig` tests DNS resolution (Application Layer), while `ping` tests basic IP reachability via ICMP (Network Layer).
- Packet switching is the foundation of the modern Internet: by breaking large data streams into independent packets, multiple computers can share the same physical cables without blocking each other.

## 5. Difficulties faced
Distinguishing why a host might respond to `dig` and `ping` but still fail to load in a web browser.

## 6. How I resolved them
Learned that `ping` uses ICMP at the network layer, whereas websites operate on TCP ports 80/443 at the transport/application layer. A server can reply to pings while its web server software (Nginx/Apache) is crashed or firewalled.

## 7. Evidence / files
- Networking diagnostic log: [`../evidence/networking-tests.log`](../evidence/networking-tests.log)
- Mission 7 documentation: [`README.md`](./README.md)
- Root README: [`../README.md`](../README.md)

## 8. Commit details
- **Commit Message:** `Add networking notes and DNS observations`
- **Branch:** `main`
- **Remote Push Status:** To be verified and pushed to `https://github.com/piushisharma/digital-detective-8410`
