SECTION_NAMES = [
    "education",
    "technical skills",
    "projects",
    "leadership & activities",
    "achievements",
    "contact",
]


def is_contact_line(line: str) -> bool:
    """
    Check whether a line contains contact information.
    """

    normalized_line = line.lower().strip()

    contact_keywords = [
        "contact -",
        "mail:",
        "linkedin-",
        "coding profiles-",
    ]

    return any(
        keyword in normalized_line
        for keyword in contact_keywords
    )


def extract_resume_sections(
    text: str,
) -> dict[str, str]:
    """
    Extract major sections from a resume.

    Contact information is detected even when it
    does not appear under a standalone heading.

    Args:
        text: Cleaned resume text.

    Returns:
        Dictionary mapping section names to their content.
    """

    lines = text.split("\n")

    sections = {}

    current_section = None
    current_content = []

    for line in lines:

        normalized_line = line.strip().lower()

        # -----------------------------------------
        # Check for standard section heading
        # -----------------------------------------

        detected_section = None

        for section_name in SECTION_NAMES:
            if normalized_line == section_name:
                detected_section = section_name
                break

        # -----------------------------------------
        # Handle "Contact - phone" line specially
        # -----------------------------------------

        if normalized_line.startswith("contact -"):

            if current_section is not None:
                sections[current_section] = "\n".join(
                    current_content
                ).strip()

            current_section = "contact"

            contact_value = line.strip()

            # Remove the "Contact -" label but
            # preserve the phone number.
            contact_value = contact_value[
                len("Contact -"): 
            ].strip()

            current_content = []

            if contact_value:
                current_content.append(
                    contact_value
                )

            continue

        # -----------------------------------------
        # Detect other contact lines
        # -----------------------------------------

        if (
            normalized_line.startswith("mail:")
            or normalized_line.startswith("linkedin-")
            or normalized_line.startswith("coding profiles-")
        ):

            if current_section != "contact":

                if current_section is not None:
                    sections[current_section] = "\n".join(
                        current_content
                    ).strip()

                current_section = "contact"
                current_content = []

            current_content.append(line.strip())

            continue

        # -----------------------------------------
        # Standard section detected
        # -----------------------------------------

        if detected_section:

            if current_section is not None:
                sections[current_section] = "\n".join(
                    current_content
                ).strip()

            current_section = detected_section
            current_content = []

            continue

        # -----------------------------------------
        # Normal content
        # -----------------------------------------

        if current_section is not None:
            current_content.append(line)

    # -----------------------------------------
    # Save final section
    # -----------------------------------------

    if current_section is not None:
        sections[current_section] = "\n".join(
            current_content
        ).strip()

    return sections