from typing import TypedDict


class MedicalState(TypedDict):

    file_path: str

    extracted_text: str

    disease: str

    rag_response: str

    final_report: str