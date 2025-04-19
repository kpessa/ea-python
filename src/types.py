from typing import List, Dict, Union, Literal, TypedDict, Optional, Any

# Using TypedDict for closer mapping to JSON structures

class BaseOrder(TypedDict):
    MNEMONIC: str
    ORDER_SENTENCE: str
    ASC_SHORT_DESCRIPTION: str # Often empty
    COMMENT: str

class RouteInfo(TypedDict):
    isOralOrTube: bool
    pillText: str

class BaseMedicationDefinition(TypedDict):
    MNEMONIC: str
    routeInfo: RouteInfo
    COMMENT: Optional[str]

class LabOrderDefinition(TypedDict):
    MNEMONIC: str
    ORDER_SENTENCE: str
    COMMENT: Optional[str]

class OrderSection(TypedDict):
    SECTION_NAME: str
    CONCEPT_NAME: str
    SINGLE_SELECT: Literal[0, 1]
    SHOW_INACTIVE_DUPLICATES: Literal[0, 1] # Usually 0
    ORDERS: List[BaseOrder] # Can be MedicationOrder or LabOrder

class ReplacementSectionConfig(TypedDict):
    sectionName: str # Often empty initially, built later
    conceptName: str
    singleSelect: Literal[0, 1]
    criticalAlertText: Optional[str]
    orders: List[Dict] # Now a list of dicts like {'predefinedMedKey': str, 'extraComment': Optional[str]}

class LabSectionConfig(TypedDict):
    conceptName: str
    associatedRouteType: Literal['Oral', 'IV', 'Peripheral', 'Central']
    sectionDescription: str
    orders: List[LabOrderDefinition] # Structure from protocol files

# Using Union for RangeInfo variants
class BetweenRangeInfo(TypedDict):
    type: Literal['between']
    electrolyte: str
    lower: float
    upper: float
    unit: str

class LessThanRangeInfo(TypedDict):
    type: Literal['lessThan']
    electrolyte: str
    level: float
    unit: str

RangeInfo = Union[BetweenRangeInfo, LessThanRangeInfo]

class SectionGroup(TypedDict):
    rangeInfo: RangeInfo
    replacementSection: ReplacementSectionConfig
    labSections: List[LabSectionConfig]
    recommendOral: Optional[bool]

class InitialLabConfig(TypedDict):
    sectionName: str
    conceptName: str
    orders: List[LabOrderDefinition]

class ProtocolData(TypedDict):
    sectionGroups: List[SectionGroup]
    initialLabs: List[InitialLabConfig]

# --- Top Level Config Interfaces ---

class ResourceUrl(TypedDict):
    LABEL: str
    URL: str

class Mnemonic(TypedDict):
    MNEMONIC: str

class ResultsView(TypedDict):
    LOOKBEHIND_LABEL: str

class GraphedResult(TypedDict):
    LABEL: str
    EVENT_SET: str
    LOOKBACK: str # e.g., '144,H'
    MAX_RESULT_COUNT: str # e.g., '6'
    RESULTS_VIEW: ResultsView

class Criterion(TypedDict):
    LABEL: str
    CONCEPT_NAME: str
    DISPLAY: str
    TOOLTIP: str

class SubmitButton(TypedDict):
    DISMISS_LABEL: str
    SIGN_LABEL: str
    
# CancelButton is just an empty dict {} in source, represented here
CancelButton = Dict[str, Any] 

class TabConfig(TypedDict):
    TAB_NAME: str
    TAB_KEY: str
    FLAG_ON_CONCEPT: str
    CONCEPT_FOR_DISMISS: str
    MNEMONICS: Optional[List[Mnemonic]]
    CONCEPTS: Optional[List[Any]] # Often empty
    CRITERIA: List[Criterion]
    GRAPHED_RESULTS: List[GraphedResult]
    RESOURCE_URLS: Optional[List[ResourceUrl]]
    SUBMIT_BUTTON: SubmitButton
    CANCEL_BUTTON: CancelButton # Usually empty dict
    ORDER_SECTIONS: List[OrderSection]

class RConfig(TypedDict):
    TABS: List[TabConfig]
    CCL_POSTPROCESS: str
    JSON_RETURN: str # Usually empty

class FullConfig(TypedDict):
    RCONFIG: RConfig

# --- Common Components Structure (as loaded from JSON/dict) ---
class CommonComponents(TypedDict):
    commonCriteria: List[Criterion]
    commonResourceUrls: List[ResourceUrl]
    commonSubmitButton: SubmitButton
    commonCancelButton: CancelButton 

# --- Generation Context ---
Protocol = Literal['REGULAR', 'CARDIAC', 'DKA']

class GenerationContext(TypedDict):
    protocol: Protocol

# RouteStyle = Literal['badge', 'bold_underline']
# showTotalDose: bool 