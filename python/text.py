import math
from typing import Union

# Helper function equivalent to Jsonnet's std.format('%.1f', level)
def format_level_for_display(level: float) -> str:
    """Formats a float to one decimal place."""
    return f"{level:.1f}"

# Helper function to create styled HTML pills
def create_pill(
    pill_text: str,
    background_color: str = '#f0f0f0',
    text_color: str = '#555',
    border_style: str = '1px solid #dcdcdc',
    show_asterisk: bool = True
) -> str:
    """Creates an HTML span element styled as a pill."""
    asterisk = '*' if show_asterisk else ''
    # Mimicking style from TypeScript version which included vertical-align
    style = (
        f"display: inline-block; "
        f"background-color: {background_color}; "
        f"color: {text_color}; "
        f"border: {border_style}; "
        f"border-radius: 3px; "
        f"padding: 2px 6px; "
        f"font-size: 12px; "
        f"font-weight: normal; "
        f"margin-top: 4px; "
        f"vertical-align: middle;"
    )
    return f'<span style="{style}">{pill_text}{asterisk}</span> '

# Helper function to format Total Dose text as HTML
def format_total_dose_text(total_dose_value: Union[int, float], dose_unit: str) -> str:
    """Creates HTML span for displaying total dose."""
    return f'<span style="font-size: 13px; color: #666;">Total Dose: {total_dose_value} {dose_unit}</span>'

# --- Exported Text Constants ---

# Style Definitions
_step_title_style = "font-size: 18px; font-weight: bold; color: #333;"
_guidance_style = "font-size: 14px; color: #666; line-height: 1.5;"
_alert_style = "background-color: #fff0f0; border-left: 3px solid #d9534f; color: #a94442; padding: 8px 12px; margin-bottom: 8px; font-weight: bold; font-size: 14px; border-radius: 3px;"

step1_text = f'<strong style="{_step_title_style}">Step 1 - Order most appropriate replacement:</strong><br>'
step2_text = f'<strong style="{_step_title_style}">Step 2 - Order corresponding follow-up lab(s):</strong><br>'

recommended_oral_text = f'<span style="{_guidance_style}">* If patient is not NPO, and tolerating oral medications, the recommended choice of replacement route is to be oral. </span> <br>'

# Pre-rendered pills
oral_route_pill = create_pill('Oral')
tube_route_pill = create_pill('Feeding Tube')
oral_tube_route_pill_lab = create_pill('Oral / Feeding Tube')
peripheral_iv_pill = create_pill('Peripheral IV', background_color='#ede9fe', text_color='#1c1f21', show_asterisk=False)
central_iv_pill = create_pill('Central IV Preferred', background_color='#ede9fe', text_color='#1c1f21', show_asterisk=False)
iv_pill = create_pill('Intravenous', background_color='#ede9fe', text_color='#1c1f21', show_asterisk=False)

asterisk_meaning_text = f'<span style="{_guidance_style}">* Oral/Tube route is preferred if patient is not NPO and tolerating PO/Tube intake.</span>'

# Alerts
critically_low_notify_physician_simple_text = f'<div style="{_alert_style}">NOTIFY PHYSICIAN<br>CRITICALLY LOW RESULT</div>'

# Function to create the specific "Notify Physician if less than X" text
def create_critically_low_notify_physician_text(level: float, unit: str) -> str:
    """Creates specific HTML text for critically low results with a threshold."""
    formatted_level = format_level_for_display(level)
    return f'<span style="color: red; font-weight: bold;">NOTIFY PHYSICIAN if less than {formatted_level} {unit}<br>CRITICALLY LOW RESULT</span> <br>'

# Note: In Jsonnet, createCriticallyLowNotifyPhysicianText was defined inside the main object.
# Here, it's a standalone function like the others. 