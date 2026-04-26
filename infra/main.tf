terraform {
  required_providers {
    harness = {
      source  = "harness/harness"
      version = "0.42.1"
    }
  }
}

provider "harness" {
  # Reads HARNESS_PLATFORM_API_KEY and HARNESS_ACCOUNT_ID from environment
}
