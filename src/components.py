from .types import Criterion, ResourceUrl, SubmitButton, CancelButton, CommonComponents
from typing import List

# Translated from common/components.jsonnet

common_criteria: List[Criterion] = [
    {
        'LABEL': 'SCr < 2.0 mg/dL',
        'CONCEPT_NAME': '[%true%]', # Placeholder concept
        'DISPLAY': '',
        'TOOLTIP': '',
    },
    {
        'LABEL': 'Not on renal replacement therapy (HD, PD, CRRT)',
        'CONCEPT_NAME': '[%true%]', # Placeholder concept
        'DISPLAY': '',
        'TOOLTIP': 'No orders for hemodialysis, peritoneal dialysis, or CRRT',
    },
    {
        'LABEL': 'Critical Care Unit or have telemetry monitoring in place (telemetry monitoring order)',
        'CONCEPT_NAME': '[%true%]', # Placeholder concept
        'DISPLAY': '',
        'TOOLTIP': 'Room type: Critical Care, PCU, Telemetry, MS (Med/Surg) with Telemetry Monitoring order',
    },
]

common_resource_urls: List[ResourceUrl] = [
    {
        'LABEL': 'Electrolyte Protocol Guideline',
        'URL': 'https://baycare1.sharepoint.com/sites/NUR/Shared%20Documents/Electrolyte%20Protocol%20Guideline.pdf',
    },
]

common_submit_button: SubmitButton = {
    'DISMISS_LABEL': 'No Orders Necessary',
    'SIGN_LABEL': 'Sign Orders',
}

common_cancel_button: CancelButton = {}

# Combining into a single dictionary for potential ease of use, similar to TS version
common_components_data: CommonComponents = {
    'commonCriteria': common_criteria,
    'commonResourceUrls': common_resource_urls,
    'commonSubmitButton': common_submit_button,
    'commonCancelButton': common_cancel_button
} 