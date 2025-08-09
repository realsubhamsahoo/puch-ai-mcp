import re

def update_section(
    existing_resume_latex: str,
    section_name: str,
    new_section_content: str,
) -> str:
    """
    Updates a specific section of an existing LaTeX resume.
    """
    # The new content should be wrapped in the same markers.
    # The user-provided content might not have the section heading, so we should ask the LLM to provide it.
    # The prompt for the tool should guide the LLM to provide the full section content, including the heading.
    replacement = f"% BEGIN_SECTION: {section_name}\n{new_section_content}\n% END_SECTION: {section_name}"

    # Create a regex pattern to find the section to be replaced.
    # The pattern looks for:
    # % BEGIN_SECTION: [section_name]
    # ... any content (non-greedy) ...
    # % END_SECTION: [section_name]
    pattern = re.compile(
        f"% BEGIN_SECTION: {re.escape(section_name)}.*?% END_SECTION: {re.escape(section_name)}",
        re.DOTALL,
    )

    # Replace the old section with the new one.
    # Use a lambda to prevent re.subn from interpreting backslashes in the replacement string.
    new_resume_latex, num_replacements = pattern.subn(lambda m: replacement, existing_resume_latex)

    if num_replacements == 0:
        # If the section is not found, we can append it to the end of the document.
        # This might be useful if the initial resume didn't include an optional section.
        # We'll add it before the `\end{document}` line if it exists.
        end_document = "\\end{document}"
        if end_document in new_resume_latex:
            new_resume_latex = new_resume_latex.replace(end_document, f"{replacement}\n\n{end_document}")
        else:
            new_resume_latex += f"\n\n{replacement}"

    return new_resume_latex
