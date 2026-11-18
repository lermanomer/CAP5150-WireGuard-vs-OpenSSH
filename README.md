# CAP 5150 Project Artifacts

This repository contains the supporting artifacts for the final CAP 5150 project comparing WireGuard VPN and OpenSSH tunneling.

The repository is organized into four main areas: configuration files, testing scripts, experimental results, and supporting screenshots.

## Repository Structure

### `configs/`

Contains configuration information for both remote-access methods.

#### `configs/wireguard/`

- `client.conf` — sanitized WireGuard remote-client configuration
- `gateway.conf` — sanitized WireGuard gateway configuration
- `firewall_rules.txt` — documents the access-control states used during the administrative tests

Private keys have been removed from the configuration files.

#### `configs/openssh/`

- `port_forwarding_commands.txt` — documents the local port-forwarding setup used to reach the five internal services and the additional forwarding used during performance testing

### `scripts/`

Contains the Python scripts used during testing.

- `tcp_echo_server.py` — small TCP echo service used for the round-trip test
- `tcp_round_trip_client.py` — measures the time required to send and receive a small TCP message
- `http_scalability_test.py` — generates the 100-request workload used for the one-service and five-service scalability tests

### `results/`

Contains the measurements used in the Evaluation & Results section of the final paper.

- `administrative_results.csv` — final administrative timing results
- `throughput_results.csv` — three final controlled iperf3 trials for each method
- `http_response_results.csv` — five HTTP response-time trials for each method
- `tcp_round_trip_results.csv` — five TCP round-trip measurements for each method
- `scalability_results.csv` — five trials for each one-service and five-service workload

The older preliminary OpenSSH throughput measurements are not included because the throughput experiment was repeated under controlled conditions. The values in `throughput_results.csv` are the final measurements used in the paper.

### `evidence/`

Contains screenshots captured during the experiments.

#### `administrative/`
Shows the access-control changes and verification performed during the administrative tests.

#### `configuration/`
Shows the WireGuard configuration and gateway firewall-rule changes.

#### `latency/`
Contains the WireGuard and OpenSSH HTTP response-time and TCP round-trip testing screenshots.

#### `scalability/`
Contains the five-run screenshots for the WireGuard and OpenSSH one-service and five-service scalability tests.

#### `throughput/`
Contains the final controlled WireGuard and OpenSSH iperf3 throughput testing screenshots.

## Relationship to the Final Report

The artifact folders correspond to the main experimental areas in the paper:

- **Administrative Effort and Access Control** → `results/administrative_results.csv` and `evidence/administrative/`
- **Throughput and HTTP Response Time** → `results/throughput_results.csv`, `results/http_response_results.csv`, `evidence/throughput/`, and `evidence/latency/`
- **TCP Round-Trip Testing** → `results/tcp_round_trip_results.csv`, `scripts/`, and `evidence/latency/`
- **Scalability Testing** → `results/scalability_results.csv`, `scripts/http_scalability_test.py`, and `evidence/scalability/`

## Security and Sanitization

Configuration files in this repository are provided for documentation and reproducibility. Private keys, passwords, SSH credentials, and other sensitive values have been removed or replaced with placeholders.

## Notes

The experiments were performed in the three-VM environment described in the final report. The CSV files contain the measurements used to calculate the values shown in the final results tables. Screenshots are included as supporting evidence of the test execution and configuration states.
