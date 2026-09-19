# OCI Workload Identity Python Access

This Python example demonstrates how an OCI workload can access OCI resources without explicit API keys, using the `ResourcePrincipalSigner`. It simulates the client-side interaction that would occur after a successful Workload Identity Federation, where an external identity (like from GitHub or Kubernetes) assumes an OCI identity and obtains temporary credentials. The code attempts to list OCI compartments, illustrating secure access based on assigned IAM policies rather than static credentials.

## Language

`python`

## How to Run

1. Install OCI SDK: `pip install oci`
2. Run in OCI: Deploy this script as an OCI Function, OCI Container Instance, or run it on an OCI Compute instance with an Instance Principal configured and appropriate IAM policies.
3. Local (will fail without specific ENV vars): Running locally will likely result in an error as `ResourcePrincipalSigner` requires specific OCI environment variables or an OCI service context. This highlights that the "no credentials" mechanism is tied to the execution environment.

## Original Article

This example accompanies the Turkish article: [OCI Workload Identity Federation: GitHub, Kubernetes ve AI İçin Kalıcı Kimlik Bilgisi Olmadan Güvenli Erişim](https://fatihsoysal.com/blog/oci-workload-identity-federation-github-kubernetes-ve-ai-icin-kalici-kimlik-bilgisi-olmadan-guvenli-erisim/).

## License

MIT — see [LICENSE](LICENSE).
