from fpdf import FPDF
import datetime

class PDFReport(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('helvetica', 'I', 8)
            self.cell(0, 10, 'AcademicHub Security Audit Report - Confidential', 0, 0, 'R')
            self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_report():
    pdf = PDFReport()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # --- PAGE 1: COVER PAGE ---
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 24)
    pdf.ln(60)
    pdf.cell(0, 20, 'System Audit & Technical Report', 0, 1, 'C')
    pdf.set_font('helvetica', 'B', 18)
    pdf.set_text_color(79, 70, 229) # Primary Color
    pdf.cell(0, 10, 'AcademicHub: Cybersecurity Educational Platform', 0, 1, 'C')
    pdf.set_text_color(0, 0, 0)
    
    pdf.ln(40)
    pdf.set_font('helvetica', '', 12)
    pdf.cell(0, 10, 'Project Type: Security-Focused MVP', 0, 1, 'C')
    pdf.cell(0, 10, f'Date: {datetime.date.today().strftime("%B %d, %Y")}', 0, 1, 'C')
    pdf.ln(20)
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(0, 10, 'Prepared by: Technical Audit Agent', 0, 1, 'C')
    pdf.cell(0, 10, 'Role: Senior Cybersecurity Engineer', 0, 1, 'C')

    # --- PAGE 2: EXECUTIVE SUMMARY & SYSTEM OVERVIEW ---
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 10, '1. Executive Summary', 0, 1, 'L')
    pdf.set_font('helvetica', '', 11)
    summary = (
        "AcademicHub is a secure, bilingual (Arabic/English) educational platform designed for "
        "academic institutions to manage course materials with high security standards. "
        "The platform addresses the critical need for internal account management and "
        "hardware-level access control in sensitive cybersecurity learning environments. "
        "By eliminating external email dependencies and implementing device-lock logic, "
        "the system significantly reduces the attack surface for credential sharing and account hijacking."
    )
    pdf.multi_cell(0, 6, summary)
    
    pdf.ln(10)
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 10, '2. System Overview', 0, 1, 'L')
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(0, 8, '2.1 Architecture', 0, 1, 'L')
    pdf.set_font('helvetica', '', 11)
    pdf.multi_cell(0, 6, 
        "The application utilizes a Client-Server architecture. The backend is built with Python/Flask, "
        "leveraging SQLite for reliable persistence. The frontend is a modern Single Page Application (SPA) "
        "built with Vanilla JavaScript, allowing for responsive interactions without full page reloads."
    )
    
    # --- PAGE 3: ROLES & AUTHENTICATION ---
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 10, '3. User Roles & Permissions', 0, 1, 'L')
    
    # Draw Table
    pdf.set_font('helvetica', 'B', 10)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(40, 10, 'Role', 1, 0, 'C', True)
    pdf.cell(150, 10, 'Capabilities', 1, 1, 'C', True)
    
    pdf.set_font('helvetica', '', 10)
    pdf.cell(40, 10, 'Administrator', 1, 0, 'C')
    pdf.cell(150, 10, 'Full Management, Create Students, Reset Devices, Manage Subjects/Files.', 1, 1, 'L')
    pdf.cell(40, 10, 'Editor', 1, 0, 'C')
    pdf.cell(150, 10, 'Upload/Delete Course Materials, AI Assistance Management.', 1, 1, 'L')
    pdf.cell(40, 10, 'Student', 1, 0, 'C')
    pdf.cell(150, 10, 'Read-only access, Download materials, AI Summary viewing.', 1, 1, 'L')
    
    pdf.ln(10)
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 10, '4. Authentication & Security Logic', 0, 1, 'L')
    pdf.set_font('helvetica', '', 11)
    pdf.multi_cell(0, 6, 
        "Unlike traditional platforms, AcademicHub uses internal identifiers (e.g., student001) instead of real emails. "
        "This prevents password recovery via external mailbox compromise.\n\n"
        "Security Policies:\n"
        "- Mandatory first-login password change.\n"
        "- Hardware Binding: One account is locked to one specific device/browser ID.\n"
        "- Server-side enforcement of all access roles via custom X-User-Role headers.\n"
        "- Password Hashing: SHA-256 with complex salt (Werkzeug)."
    )

    # --- PAGE 4: CONTENT MANAGEMENT & ADMIN CONTROL ---
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 10, '5. Subject & File Management', 0, 1, 'L')
    pdf.set_font('helvetica', '', 11)
    pdf.multi_cell(0, 6,
        "Admins can create Subjects with unique codes and visual themes. Files uploaded are saved to a secured "
        "disk directory with timestamped, non-predictable filenames. Deleting a subject or file in the UI "
        "triggers a physical purge from the server disk, ensuring zero data remnants."
    )
    
    pdf.ln(10)
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 10, '6. Admin Control Panel', 0, 1, 'L')
    pdf.set_font('helvetica', '', 11)
    pdf.multi_cell(0, 6,
        "The Admin Dashboard provides real-time status of student accounts (Linked vs. Pending). "
        "It includes specialized 'Device Reset' buttons to handle student hardware migrations and "
        "'Force Password Reset' for account recovery."
    )

    # --- PAGE 5: CODE STRUCTURE & AUDIT ---
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 10, '7. Code Structure & Modules', 0, 1, 'L')
    pdf.set_font('helvetica', 'B', 10)
    pdf.cell(50, 8, 'File', 1, 0, 'C', True)
    pdf.cell(140, 8, 'Purpose', 1, 1, 'C', True)
    
    pdf.set_font('helvetica', '', 10)
    files = [
        ("app.py", "Flask Backend: Routes, Database, File Storage, Auth."),
        ("api.js", "Client-Side API: Handles fetch requests with security headers."),
        ("main.js", "Router: SPA Navigation and Navigation UI updates."),
        ("i18n.js", "Internationalization: Dual-language (AR/EN) state."),
        ("ui.js", "UI Components: Reusable Modals/Toasts logic."),
        ("AdminPage.js", "Administrative Dashboard & Student Control UI."),
        ("SubjectPage.js", "Course Content & AI Summary Integration."),
    ]
    for f, p in files:
        pdf.cell(50, 8, f, 1, 0, 'L')
        pdf.cell(140, 8, p, 1, 1, 'L')
        
    pdf.ln(10)
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 10, '8. Bugs Found & Mitigations', 0, 1, 'L')
    pdf.set_font('helvetica', '', 11)
    pdf.multi_cell(0, 6,
        "- Bug: Insecure API routes (Fixed by adding server-side @require_role decorators).\n"
        "- Bug: Unauthorized Role Escalation (Fixed by protecting user role update endpoints).\n"
        "- Bug: Invalid Admin role in DB (Fixed via direct SQL migration script).\n"
        "- Bug: Device ID mismatch on incognito (Fixed by binding on first success login).\n"
        "- Bug: Gemini Model 404 (Fixed by switching to stable gemini-1.5-flash endpoint)."
    )

    # --- PAGE 6: FINAL ASSESSMENT ---
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 10, '9. AI Features Analysis', 0, 1, 'L')
    pdf.set_font('helvetica', '', 11)
    pdf.multi_cell(0, 6,
        "The platform is integrated with Google Gemini 1.5 Flash AI. It provides:\n"
        "- Full PDF text extraction and analysis.\n"
        "- Comprehensive bilingual (Arabic/English) lecture summarization.\n"
        "- Automated study question generation in both languages.\n"
        "- Context-aware academic assistance based on course materials."
    )

    pdf.ln(10)
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 10, '10. Final Assessment', 0, 1, 'L')
    pdf.set_font('helvetica', 'B', 12)
    pdf.set_text_color(0, 128, 0) # Green for success
    pdf.cell(0, 10, 'READY FOR DEMO / PRODUCTION PILOT', 0, 1, 'C')
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('helvetica', '', 11)
    pdf.multi_cell(0, 6,
        "Conclusion: The system is structurally sound, secure against common hijacking "
        "attacks, and provides a professional UI/UX. It serves as a robust MVP for "
        "cybersecurity academic departments."
    )

    pdf.output("AcademicHub_Project_Report.pdf")
    print("PDF Report Generated Successfully: AcademicHub_Project_Report.pdf")

if __name__ == "__main__":
    generate_report()
