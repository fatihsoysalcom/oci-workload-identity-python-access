import oci
import os

def main():
    print("Attempting to access OCI Identity service using Resource Principal Signer...")
    print("This simulates a workload (like a federated identity) accessing OCI without explicit API keys.")

    try:
        # The ResourcePrincipalSigner automatically picks up credentials from the OCI environment.
        # This is analogous to how a federated identity, after successful token exchange,
        # would interact with OCI services using temporary credentials provided by OCI.
        # It requires specific environment variables (e.g., OCI_RESOURCE_PRINCIPAL_VERSION, OCI_RESOURCE_PRINCIPAL_REGION)
        # to be set, which are automatically available when running inside OCI services
        # like OCI Functions, Container Instances, or Compute instances with Instance Principals.
        signer = oci.auth.signers.get_resource_principal_signer()

        # Initialize the IdentityClient using the resource principal signer
        identity_client = oci.identity.IdentityClient({}, signer=signer)

        # List compartments (a basic OCI operation)
        # This operation requires appropriate IAM policies to be set for the resource principal.
        print("\nSuccessfully initialized OCI Identity Client with Resource Principal.")
        print("Listing up to 5 compartments (requires 'inspect compartments' permission)...\n")

        list_compartments_response = identity_client.list_compartments(
            compartment_id=signer.tenancy_id,
            compartment_id_in_subtree=True,
            access_level="ACCESSIBLE",
            lifecycle_state="ACTIVE"
        )

        compartments = list_compartments_response.data
        if compartments:
            print(f"Found {len(compartments)} active compartments (showing first 5):")
            for i, compartment in enumerate(compartments[:5]):
                print(f"  - Name: {compartment.name}, ID: {compartment.id}")
        else:
            print("No active compartments found or accessible.")

    except oci.exceptions.ServiceError as e:
        print(f"\nOCI Service Error: {e}")
        print("This often means the resource principal does not have the necessary IAM permissions.")
        print("Ensure the resource principal (or the federated identity it represents) has policies like:")
        print("  'Allow dynamic-group <your_dynamic_group> to inspect compartments in tenancy'")
    except Exception as e:
        print(f"\nError: {e}")
        print("This example requires running within an OCI service (e.g., OCI Functions, Container Instances, or a Compute instance with Instance Principal enabled) or having the necessary OCI_RESOURCE_PRINCIPAL_* environment variables set for local testing.")
        print("Workload Identity Federation aims to provide a similar 'no credentials' experience for external workloads.")
        print("For local development, consider using OCI config file authentication or environment variables.")

if __name__ == "__main__":
    main()
