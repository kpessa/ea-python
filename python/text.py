import math
from typing import Union

# Helper function equivalent to Jsonnet's std.format('%.1f', level)
def format_level_for_display(level: float) -> str:
    """Formats a float to one decimal place."""
    return f"{level:.1f}"

# --- Exported Text Constants ---

# Style Definitions
_step_title_style = "font-size: 18px; font-weight: bold; color: #333;"
_guidance_style = "font-size: 14px; color: #666; line-height: 1.5;"
_notify_provider_style = "color: red; font-weight: bold; font-size: 14px;"

step1_text = f'<strong style="{_step_title_style}">Step 1 - Order most appropriate replacement:</strong><br>'
step2_text = f'<strong style="{_step_title_style}">Step 2 - Order corresponding follow-up lab(s):</strong><br>'

recommended_oral_text = f'<span style="{_guidance_style}">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>'

# Alerts
notify_provider_simple_text = f'<span style="{_notify_provider_style}">NOTIFY PHYSICIAN</span><br>'

# Function to create the specific "Notify Physician if less than X" text
def create_notify_provider_text(level: float, unit: str) -> str:
    """Creates specific HTML text for results requiring provider notification.

    >>> create_notify_provider_text(1.2, 'mg/dL')
    '<span style="color: red; font-weight: bold; font-size: 14px;">NOTIFY PHYSICIAN if less than 1.2 mg/dL</span><br>'
    >>> create_notify_provider_text(2.8, 'mmol/L')
    '<span style="color: red; font-weight: bold; font-size: 14px;">NOTIFY PHYSICIAN if less than 2.8 mmol/L</span><br>'
    """
    formatted_level = format_level_for_display(level)
    return f'<span style="{_notify_provider_style}">NOTIFY PHYSICIAN if less than {formatted_level} {unit}</span><br>'

# Note: In Jsonnet, createCriticallyLowNotifyPhysicianText was defined inside the main object.
# Here, it's a standalone function like the others. 

# --- Common Timed Lab Comments ---

timed_lab_comment_k_oral = "Recheck potassium level 4 hrs after last dose."
timed_lab_comment_k_iv = "Recheck potassium level 1 hr after infusion complete." 