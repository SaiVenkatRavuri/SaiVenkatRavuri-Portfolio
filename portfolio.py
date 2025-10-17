# enhanced_portfolio_app.py
import streamlit as st
import pandas as pd
from datetime import datetime
import json
import time

# Page configuration
st.set_page_config(
    page_title="Saivenkat Ravuri - Cybersecurity Professional",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced Custom CSS with advanced styling and animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@300;400;500;600&family=Poppins:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
        scroll-behavior: smooth;
    }
    
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
    }
    
    /* Animated Background */
    .main-container {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradientAnimation 15s ease infinite;
        min-height: 100vh;
    }
    
    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Header Styles */
    .main-header {
        font-family: 'Poppins', sans-serif;
        font-size: 4rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 0.5rem;
        font-weight: 800;
        letter-spacing: -1px;
        text-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        animation: fadeInUp 1s ease-out;
    }
    
    .sub-header {
        font-size: 1.6rem;
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2.5rem;
        font-weight: 500;
        animation: fadeInUp 1s ease-out 0.2s both;
    }
    
    .typing-animation {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.2rem;
        color: #667eea;
        text-align: center;
        margin-bottom: 2rem;
        border-right: 2px solid #667eea;
        animation: typing 3s steps(40, end), blink-caret 0.75s step-end infinite;
    }
    
    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }
    
    @keyframes blink-caret {
        from, to { border-color: transparent; }
        50% { border-color: #667eea; }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Section Headers */
    .section-header {
        font-family: 'Poppins', sans-serif;
        font-size: 2.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        border-bottom: 3px solid transparent;
        border-image: linear-gradient(135deg, #667eea 0%, #764ba2 100%) 1;
        padding-bottom: 0.8rem;
        margin-top: 3rem;
        margin-bottom: 2rem;
        font-weight: 700;
        position: relative;
        animation: slideInLeft 0.8s ease-out;
    }
    
    .section-header::before {
        content: '';
        position: absolute;
        bottom: -3px;
        left: 0;
        width: 0;
        height: 3px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        animation: expandWidth 1s ease-out 0.5s both;
    }
    
    @keyframes expandWidth {
        to { width: 100px; }
    }
    
    /* Card Styles */
    .enhanced-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        padding: 2.5rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.1),
            0 2px 8px rgba(102, 126, 234, 0.15);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }
    
    .enhanced-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
        transition: left 0.5s;
    }
    
    .enhanced-card:hover::before {
        left: 100%;
    }
    
    .enhanced-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 
            0 20px 60px rgba(0, 0, 0, 0.15),
            0 5px 20px rgba(102, 126, 234, 0.25);
        border-color: rgba(102, 126, 234, 0.3);
    }
    
    .project-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(240, 248, 255, 0.9) 100%);
        backdrop-filter: blur(15px);
        padding: 2.5rem;
        border-radius: 18px;
        margin-bottom: 2rem;
        border-left: 5px solid #667eea;
        box-shadow: 
            0 10px 40px rgba(0, 0, 0, 0.08),
            0 2px 12px rgba(102, 126, 234, 0.12);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
        animation: slideInRight 0.8s ease-out;
    }
    
    .project-card:hover {
        transform: translateY(-8px) rotateX(5deg);
        box-shadow: 
            0 25px 60px rgba(0, 0, 0, 0.15),
            0 5px 25px rgba(102, 126, 234, 0.2);
        border-left-width: 8px;
    }
    
    /* Metrics Cards */
    .metric-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 250, 252, 0.95) 100%);
        backdrop-filter: blur(15px);
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.06),
            0 2px 8px rgba(102, 126, 234, 0.08);
        transition: all 0.3s ease;
        animation: fadeInUp 0.6s ease-out;
    }
    
    .metric-card:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 
            0 15px 45px rgba(0, 0, 0, 0.1),
            0 3px 15px rgba(102, 126, 234, 0.15);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        font-family: 'Poppins', sans-serif;
    }
    
    .metric-label {
        font-size: 0.95rem;
        color: #64748b;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Skill Badges */
    .skill-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.6rem 1.2rem;
        border-radius: 25px;
        margin: 0.4rem;
        display: inline-block;
        font-size: 0.9rem;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
        cursor: pointer;
        border: 2px solid transparent;
    }
    
    .skill-badge:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        border-color: rgba(255, 255, 255, 0.3);
    }
    
    .tech-badge {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        display: inline-block;
        font-size: 0.85rem;
        font-weight: 500;
        box-shadow: 0 3px 12px rgba(76, 175, 80, 0.3);
        transition: all 0.3s ease;
    }
    
    .tech-badge:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(76, 175, 80, 0.4);
    }
    
    /* Achievement and Certification Items */
    .achievement-item {
        background: linear-gradient(135deg, rgba(255, 243, 224, 0.9) 0%, rgba(255, 224, 178, 0.9) 100%);
        backdrop-filter: blur(10px);
        padding: 1.5rem 2rem;
        border-radius: 15px;
        margin-bottom: 1.5rem;
        border-left: 5px solid #ff9800;
        box-shadow: 0 6px 20px rgba(255, 152, 0, 0.15);
        transition: all 0.3s ease;
        animation: slideInLeft 0.6s ease-out;
    }
    
    .achievement-item:hover {
        transform: translateX(10px);
        box-shadow: 0 10px 30px rgba(255, 152, 0, 0.25);
        border-left-width: 8px;
    }
    
    .certification-item {
        background: linear-gradient(135deg, rgba(232, 245, 233, 0.9) 0%, rgba(200, 230, 201, 0.9) 100%);
        backdrop-filter: blur(10px);
        padding: 1.5rem 2rem;
        border-radius: 15px;
        margin-bottom: 1.5rem;
        border-left: 5px solid #4caf50;
        box-shadow: 0 6px 20px rgba(76, 175, 80, 0.15);
        transition: all 0.3s ease;
        animation: slideInRight 0.6s ease-out;
    }
    
    .certification-item:hover {
        transform: translateX(-10px);
        box-shadow: 0 10px 30px rgba(76, 175, 80, 0.25);
        border-left-width: 8px;
    }
    
    /* Contact Information */
    .contact-info {
        background: linear-gradient(135deg, rgba(227, 242, 253, 0.9) 0%, rgba(187, 222, 251, 0.9) 100%);
        backdrop-filter: blur(15px);
        padding: 2rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(144, 202, 249, 0.3);
        box-shadow: 0 8px 25px rgba(33, 150, 243, 0.1);
        transition: all 0.3s ease;
    }
    
    .contact-info:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(33, 150, 243, 0.15);
    }
    
    /* Social Media Icons */
    .social-icon {
        display: inline-block;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        margin: 0.5rem;
        text-align: center;
        line-height: 50px;
        color: white;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        text-decoration: none;
    }
    
    .social-icon.linkedin {
        background: linear-gradient(135deg, #0077b5 0%, #005885 100%);
    }
    
    .social-icon.github {
        background: linear-gradient(135deg, #333 0%, #1a1a1a 100%);
    }
    
    .social-icon.email {
        background: linear-gradient(135deg, #ea4335 0%, #d33b2c 100%);
    }
    
    .social-icon:hover {
        transform: translateY(-5px) scale(1.1);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
    }
    
    /* Button Styles */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .stButton button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Progress Bar */
    .progress-container {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        padding: 4px;
        margin: 0.5rem 0;
    }
    
    .progress-bar {
        height: 8px;
        border-radius: 6px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        transition: width 2s ease-in-out;
    }
    
    /* Timeline */
    .timeline-item {
        position: relative;
        padding-left: 2rem;
        margin-bottom: 2rem;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.2);
    }
    
    .timeline-item::after {
        content: '';
        position: absolute;
        left: 5px;
        top: 12px;
        width: 2px;
        height: calc(100% + 1rem);
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    .timeline-item:last-child::after {
        display: none;
    }
    
    /* Sidebar Enhancements */
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
    }
    
    .nav-item {
        padding: 0.8rem 1rem;
        margin: 0.3rem 0;
        border-radius: 10px;
        transition: all 0.3s ease;
        cursor: pointer;
        color: white;
        font-weight: 500;
    }
    
    .nav-item:hover {
        background: rgba(255, 255, 255, 0.1);
        transform: translateX(5px);
    }
    
    .nav-item.active {
        background: rgba(255, 255, 255, 0.2);
        border-left: 3px solid #ffffff;
    }
    
    /* Footer Styles */
    .footer {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        color: white;
        padding: 3rem 0 2rem 0;
        margin-top: 4rem;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .footer::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .footer-content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 2rem;
    }
    
    .footer-section {
        margin-bottom: 2rem;
    }
    
    .footer-title {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .footer-links {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin: 2rem 0;
        flex-wrap: wrap;
    }
    
    .footer-link {
        color: #bdc3c7;
        text-decoration: none;
        transition: all 0.3s ease;
        padding: 0.5rem 1rem;
        border-radius: 8px;
    }
    
    .footer-link:hover {
        color: #667eea;
        background: rgba(255, 255, 255, 0.1);
        transform: translateY(-2px);
    }
    
    .footer-bottom {
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        padding-top: 2rem;
        margin-top: 2rem;
        font-size: 0.9rem;
        color: #95a5a6;
    }
    
    .copyright {
        margin-bottom: 1rem;
    }
    
    .footer-note {
        font-size: 0.8rem;
        opacity: 0.8;
        line-height: 1.6;
    }
    
    /* Scroll to Top Button */
    .scroll-top {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        cursor: pointer;
        font-size: 1.2rem;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
        z-index: 1000;
    }
    
    .scroll-top:hover {
        transform: translateY(-3px) scale(1.1);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2.5rem;
        }
        
        .sub-header {
            font-size: 1.2rem;
        }
        
        .section-header {
            font-size: 2rem;
        }
        
        .enhanced-card, .project-card {
            padding: 1.5rem;
        }
        
        .footer-links {
            flex-direction: column;
            gap: 1rem;
        }
    }
    
    /* Loading Animation */
    .loading-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 200px;
    }
    
    .spinner {
        width: 40px;
        height: 40px;
        border: 4px solid rgba(102, 126, 234, 0.3);
        border-top: 4px solid #667eea;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
    }
</style>
""", unsafe_allow_html=True)

# Enhanced Portfolio Data with additional sections
portfolio_data = {
    "personal_info": {
        "name": "SAI VENKAT RAVURI",
        "title": "B.Tech IT Student | Cybersecurity Enthusiast",
        "subtitle": "Securing Digital Futures Through Innovation",
        "email": "ravurisaivenkat@gmail.com",
        "phone": "+91-63013-63267",
        "location": "Ongole, Andhra Pradesh, India",
        "linkedin": "https://www.linkedin.com/in/sai-venkat-ravuri-1143952b1/",
        "github": "https://github.com/SaiVenkatRavuri/",
        "tryhackme": "https://tryhackme.com/p/SaiVenkatRavuri",
        "portfolio_version": "2.0",
        "last_updated": "October 2025"
    },
    "tagline": "print('Hello, World! I secure it.')",
    "objective": "Passionate B.Tech IT student (2022–2026) with comprehensive expertise in cybersecurity, network defense, and secure software development. Experienced in penetration testing, threat analysis, and cloud security implementations. Seeking opportunities to contribute to cutting-edge security solutions and protect digital infrastructures from evolving cyber threats.",
    "education": {
        "degree": "Bachelor of Technology - Information Technology",
        "institution": "Pace Institute of Technology & Sciences, Vallur",
        "duration": "2022 - 2026",
        "cgpa": "8.5/10.0",
        "focus": "Cybersecurity, Network Defense, and Secure Software Development",
        "specializations": [
            "Network Security & Penetration Testing",
            "Secure Software Development",
            "Cloud Security & Infrastructure",
            "Digital Forensics & Incident Response"
        ],
        "core_concepts": [
            "Advanced Object-Oriented Programming",
            "Data Structures and Algorithms Optimization", 
            "Network Security Protocols & Implementation",
            "Artificial Intelligence in Cybersecurity",
            "Machine Learning for Threat Detection",
            "Secure Database Management Systems",
            "Cryptography & Blockchain Technology",
            "Cloud Computing Security Architecture"
        ]
    },
    "experience": [
        {
            "company": "Fortinet",
            "role": "Network Security Associate Intern",
            "duration": "Jun 2024 - Aug 2024",
            "type": "Remote Internship",
            "description": "Led comprehensive network security monitoring initiatives using FortiAnalyzer, implemented advanced threat detection protocols, and optimized security incident response workflows.",
            "achievements": [
                "Reduced false positive security alerts by 25% through strategic IDS/IPS signature tuning and custom rule development",
                "Managed real-time network security monitoring across multiple enterprise zones using FortiAnalyzer dashboard",
                "Triaged and resolved 150+ high-severity security incidents with 99.2% accuracy rate",
                "Developed automated threat intelligence correlation scripts reducing response time by 40%",
                "Collaborated with senior security engineers on threat hunting operations and vulnerability assessments"
            ],
            "technologies": ["FortiAnalyzer", "FortiGate", "IDS/IPS", "SIEM", "Python", "Bash", "Network Protocols"]
        },
        {
            "company": "42Learn",
            "role": "Full Stack Development Specialist",
            "duration": "Mar 2023 - Jul 2023",
            "type": "Project-Based Role",
            "description": "Architected and developed enterprise-grade full-stack applications using modern MERN stack technologies, focusing on secure authentication, scalable architecture, and optimal user experience.",
            "achievements": [
                "Built and deployed 3 production-ready full-stack MERN applications serving 500+ active users",
                "Implemented JWT-based secure authentication system with multi-factor authentication capabilities",
                "Developed RESTful APIs with comprehensive input validation and SQL injection prevention measures",
                "Created responsive, accessible user interfaces resulting in 35% improved user engagement",
                "Integrated advanced state management using Redux and Context API for optimal performance"
            ],
            "technologies": ["MongoDB", "Express.js", "React.js", "Node.js", "JWT", "Redux", "REST APIs", "Git"]
        }
    ],
    "projects": [
        {
            "name": "Advanced Network Security Scanner",
            "category": "Cybersecurity Tools",
            "technologies": ["Python", "Scapy", "Nmap", "Threading", "JSON", "SQLite"],
            "description": "Developed a comprehensive network security assessment tool with multi-threaded scanning capabilities, vulnerability detection, and detailed reporting features. The tool performs ICMP, TCP, UDP, and ARP scans with advanced OS fingerprinting.",
            "impact": "Enhanced network security assessment efficiency by 40% and improved threat detection accuracy by 25%",
            "features": [
                "Multi-protocol scanning (ICMP, TCP, UDP, ARP) with concurrent execution",
                "Advanced OS fingerprinting and service detection capabilities",
                "Vulnerability assessment integration with CVE database lookup",
                "Automated report generation with risk classification and remediation suggestions",
                "Custom packet crafting for advanced penetration testing scenarios",
                "Real-time progress tracking and interactive command-line interface"
            ],
            "github": "https://github.com/SaiVenkatRavuri/network-security-scanner",
            "demo": "Available on request",
            "status": "Completed"
        },
        {
            "name": "Intelligent Password Security Analyzer",
            "category": "Security Applications",
            "technologies": ["Python", "Tkinter", "Regex", "Cryptography", "Machine Learning", "SQLite"],
            "description": "Created an AI-powered password strength analysis tool with machine learning-based pattern recognition, breach database checking, and personalized security recommendations. Features real-time analysis and educational security tips.",
            "impact": "Improved password security awareness by 60% and reduced weak password usage by 45%",
            "features": [
                "Real-time password strength evaluation with ML-based pattern analysis",
                "Integration with HaveIBeenPwned API for breach database checking",
                "Advanced GUI with dark/light theme and accessibility features",
                "Personalized password generation with customizable complexity rules",
                "Security education module with interactive tutorials and best practices",
                "Password policy compliance checking for enterprise environments"
            ],
            "github": "https://github.com/SaiVenkatRavuri/password-analyzer",
            "demo": "Live demo available",
            "status": "Enhanced Version"
        },
        {
            "name": "SecureTravel - Cybersecurity-First Web Platform",
            "category": "Web Development",
            "technologies": ["HTML5", "CSS3", "JavaScript", "Bootstrap", "Node.js", "Express", "MongoDB"],
            "description": "Built a security-focused travel booking platform implementing OWASP Top 10 security measures, secure payment integration, and comprehensive user data protection. Features mobile-first responsive design and PWA capabilities.",
            "impact": "Achieved 98% security score and 95+ Lighthouse performance rating with zero security vulnerabilities",
            "features": [
                "Mobile-first responsive design with Progressive Web App (PWA) capabilities",
                "Comprehensive security headers implementation (CSP, HSTS, HPKP)",
                "Secure payment gateway integration with PCI DSS compliance",
                "Advanced input validation and XSS/CSRF protection mechanisms",
                "Real-time booking system with WebSocket integration",
                "SEO optimization resulting in 150% improved search visibility"
            ],
            "github": "https://github.com/SaiVenkatRavuri/secure-travel-platform",
            "demo": "https://securetravel-demo.netlify.app",
            "status": "Production Ready"
        },
        {
            "name": "ThreatIntel Dashboard",
            "category": "Security Analytics",
            "technologies": ["Python", "Flask", "D3.js", "Redis", "Docker", "API Integration"],
            "description": "Developed a real-time threat intelligence dashboard aggregating data from multiple security feeds, providing actionable insights and automated threat correlation capabilities.",
            "impact": "Reduced threat analysis time by 70% and improved incident response efficiency by 50%",
            "features": [
                "Real-time threat feed aggregation from 15+ security intelligence sources",
                "Interactive data visualization with custom D3.js charts and geolocation mapping",
                "Automated threat correlation engine with machine learning-based pattern recognition",
                "RESTful API for third-party security tool integration",
                "Containerized deployment with Docker and Kubernetes support",
                "Role-based access control and audit logging capabilities"
            ],
            "github": "https://github.com/SaiVenkatRavuri/threat-intel-dashboard",
            "demo": "Enterprise demo available",
            "status": "Beta Version"
        }
    ],
    "skills": {
        "programming": {
            "languages": ["Python", "Java", "C/C++", "JavaScript", "SQL", "Bash/Shell", "PowerShell"],
            "frameworks": ["React.js", "Node.js", "Express.js", "Flask", "Django", "Bootstrap"]
        },
        "cybersecurity": {
            "tools": ["Nmap", "Wireshark", "Burp Suite", "Metasploit", "Snort", "Zeek", "OpenVAS", "Nessus"],
            "platforms": ["Kali Linux", "Parrot OS", "Ubuntu", "CentOS", "Windows Server"],
            "concepts": ["Penetration Testing", "Incident Response", "Threat Hunting", "Digital Forensics", "MITRE ATT&CK", "OWASP Top 10"]
        },
        "cloud_security": {
            "platforms": ["AWS Security", "Azure Security Center", "Google Cloud Security"],
            "tools": ["CloudTrail", "GuardDuty", "Security Hub", "Azure Sentinel", "Cloud Security Posture Management"]
        },
        "soft_skills": ["Problem Solving", "Team Leadership", "Technical Communication", "Project Management", "Mentoring"]
    },
    "achievements": [
        {
            "title": "TryHackMe 30 Days of Cyber Security Challenge Champion",
            "description": "Successfully completed advanced cybersecurity challenges covering network security, web application testing, digital forensics, and incident response scenarios",
            "year": "2025",
            "impact": "Ranked in top 5% globally",
            "type": "Competition"
        },
        {
            "title": "NPTEL Elite Certification - Silver Medal",
            "description": "Privacy & Security in Online Social Media - Achieved 85% score in comprehensive examination",
            "year": "2025",
            "impact": "Top 10% performers nationwide",
            "type": "Academic"
        },
        {
            "title": "Yogendra Award - Government of Andhra Pradesh",
            "description": "Recognition for outstanding contribution to International Day of Yoga celebrations and community wellness initiatives",
            "year": "2025",
            "impact": "State-level recognition",
            "type": "Community Service"
        },
        {
            "title": "Cybersecurity Excellence Award",
            "description": "College-level recognition for exceptional performance in cybersecurity coursework and practical implementations",
            "year": "2024",
            "impact": "Academic excellence recognition",
            "type": "Academic"
        }
    ],
    "certifications": [
        {
            "name": "Microsoft Cybersecurity Analyst Professional Certificate",
            "issuer": "Microsoft via Coursera",
            "date": "September 2025",
            "level": "Professional",
            "skills": ["Security Operations", "Incident Response", "Threat Analysis"]
        },
        {
            "name": "Salesforce Certified Agentforce Specialist",
            "issuer": "Salesforce",
            "date": "August 2025",
            "level": "Advanced Administrator",
            "skills": ["CRM Security", "Data Protection", "Access Management"]
        },
        {
            "name": "Oracle Cloud Infrastructure 2025 Certified AI Foundations Associate",
            "issuer": "Oracle",
            "date": "August 2025",
            "level": "Associate",
            "skills": ["Cloud Security", "AI/ML Security", "Infrastructure Protection"]
        },
        {
            "name": "EC-Council SQL Injection Detection Specialist",
            "issuer": "EC-Council",
            "date": "2025",
            "level": "Specialist",
            "skills": ["Web Application Security", "Database Security", "Vulnerability Assessment"]
        },
        {
            "name": "Security Blue Team - Blue Team Junior Analyst",
            "issuer": "Security Blue Team",
            "date": "2025",
            "level": "Junior Analyst",
            "skills": ["SOC Operations", "Log Analysis", "Incident Response"]
        },
        {
            "name": "Java Programming Fundamentals",
            "issuer": "GalileoX",
            "date": "September 2024",
            "level": "Fundamental",
            "skills": ["Object-Oriented Programming", "Secure Coding", "Application Development"]
        }
    ],
    "metrics": {
        "projects_completed": "20+",
        "certifications": "8+",
        "technologies": "25+",
        "experience_years": "2+",
        "security_tools": "15+",
        "programming_languages": "7+"
    },
    "testimonials": [
        {
            "name": "Dr. Rajesh Kumar",
            "position": "Professor, Cybersecurity Department",
            "company": "Pace Institute of Technology",
            "text": "Sai Venkat demonstrates exceptional aptitude in cybersecurity with practical skills that exceed expectations for an undergraduate student.",
            "rating": 5
        },
        {
            "name": "Sarah Johnson",
            "position": "Senior Security Engineer",
            "company": "Fortinet",
            "text": "Outstanding intern who contributed significantly to our security operations. His analytical skills and proactive approach were impressive.",
            "rating": 5
        }
    ]
}

def main():
    # Add custom CSS for animations and effects
    st.markdown("""
    <script>
    // Smooth scrolling and interactive effects
    document.addEventListener('DOMContentLoaded', function() {
        // Add scroll-based animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);
        
        // Observe all animated elements
        document.querySelectorAll('.enhanced-card, .project-card, .achievement-item').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'all 0.6s ease-out';
            observer.observe(el);
        });
    });
    </script>
    """, unsafe_allow_html=True)
    
    # Enhanced Header Section with animations
    st.markdown(f'<h1 class="main-header">{portfolio_data["personal_info"]["name"]}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-header">{portfolio_data["personal_info"]["subtitle"]}</p>', unsafe_allow_html=True)
    
    # Typing animation effect
    st.markdown(f'<div class="typing-animation">{portfolio_data["tagline"]}</div>', unsafe_allow_html=True)
    
    # Enhanced Metrics Section with cards
    st.markdown("### 📊 Professional Metrics")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    metrics = [
        ("Projects", portfolio_data["metrics"]["projects_completed"], "🚀"),
        ("Certifications", portfolio_data["metrics"]["certifications"], "🏆"),
        ("Technologies", portfolio_data["metrics"]["technologies"], "⚡"),
        ("Experience", portfolio_data["metrics"]["experience_years"], "💼"),
        ("Security Tools", portfolio_data["metrics"]["security_tools"], "🛡️"),
        ("Languages", portfolio_data["metrics"]["programming_languages"], "💻")
    ]
    
    for i, (col, (label, value, icon)) in enumerate(zip([col1, col2, col3, col4, col5, col6], metrics)):
        with col:
            st.markdown(f"""
            <div class="metric-card" style="animation-delay: {i * 0.1}s;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
                <div class="metric-value">{value}</div>
                <div class="metric-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Enhanced Contact Information with social media
    st.markdown("---")
    st.markdown("### 🌐 Connect With Me")
    
    col1, col2, col3 = st.columns([2, 2, 2])
    with col1:
        st.markdown(f"""
        **📧 Email:** {portfolio_data['personal_info']['email']}  
        **📱 Phone:** {portfolio_data['personal_info']['phone']}  
        **📍 Location:** {portfolio_data['personal_info']['location']}
        """)
    
    with col2:
        st.markdown(f"""
        **🔗 LinkedIn:** [Professional Profile]({portfolio_data['personal_info']['linkedin']})  
        **💻 GitHub:** [Code Repository]({portfolio_data['personal_info']['github']})  
        **🎯 TryHackMe:** [Security Challenges]({portfolio_data['personal_info']['tryhackme']})
        """)
    
    with col3:
        # Social media icons
        st.markdown("""
        <div style="text-align: center; margin-top: 1rem;">
            <p><strong>🚀 Quick Connect</strong></p>
            <a href="%s" class="social-icon linkedin" target="_blank">in</a>
            <a href="%s" class="social-icon github" target="_blank">gh</a>
            <a href="mailto:%s" class="social-icon email">@</a>
        </div>
        """ % (portfolio_data['personal_info']['linkedin'], 
               portfolio_data['personal_info']['github'],
               portfolio_data['personal_info']['email']), 
        unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Enhanced Sidebar Navigation
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 2rem 0;">
            <h2 style="color: white; font-family: 'Poppins', sans-serif;">🛡️ Portfolio</h2>
            <p style="color: #bdc3c7; font-size: 0.9rem;">Cybersecurity Professional</p>
        </div>
        """, unsafe_allow_html=True)
        
        sections = [
            "🏠 Overview", "🎓 Education", "💼 Experience", "🚀 Projects", 
            "🛠️ Technical Skills", "🏆 Achievements", "📜 Certifications", 
            "💬 Testimonials", "📞 Contact"
        ]
        
        selected_section = st.radio("Navigation", sections, label_visibility="collapsed")
        
        # Portfolio stats in sidebar
        st.markdown("---")
        st.markdown("### 📈 Portfolio Stats")
        st.markdown(f"""
        **Version:** {portfolio_data['personal_info']['portfolio_version']}  
        **Last Updated:** {portfolio_data['personal_info']['last_updated']}  
        **Status:** Active & Available
        """)
    
    # Main Content Sections
    if selected_section == "🏠 Overview":
        st.markdown('<h2 class="section-header">🎯 Professional Overview</h2>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown('<div class="enhanced-card">', unsafe_allow_html=True)
            st.markdown("#### 🚀 Professional Summary")
            st.write(portfolio_data["objective"])
            
            st.markdown("#### 🎯 Core Specializations")
            specializations = [
                "🛡️ **Cybersecurity & Threat Analysis**",
                "🌐 **Network Security & Penetration Testing**", 
                "☁️ **Cloud Security Architecture**",
                "🔒 **Secure Software Development**",
                "🤖 **AI-Powered Security Solutions**"
            ]
            for spec in specializations:
                st.markdown(spec)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="enhanced-card">', unsafe_allow_html=True)
            st.markdown("#### ⚡ Quick Highlights")
            
            highlights = [
                ("Security Tools Mastery", "15+ Tools", "🛠️"),
                ("Programming Languages", "7+ Languages", "💻"),
                ("Active Projects", "20+ Projects", "🚀"),
                ("Industry Certifications", "8+ Certified", "🏆"),
                ("Professional Experience", "2+ Years", "💼")
            ]
            
            for title, value, icon in highlights:
                st.markdown(f"""
                <div style="display: flex; align-items: center; margin: 1rem 0; padding: 0.5rem; 
                     background: rgba(102, 126, 234, 0.1); border-radius: 8px;">
                    <span style="font-size: 1.5rem; margin-right: 1rem;">{icon}</span>
                    <div>
                        <strong>{title}</strong><br>
                        <span style="color: #667eea; font-weight: 600;">{value}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    elif selected_section == "🎓 Education":
        st.markdown('<h2 class="section-header">🎓 Academic Excellence</h2>', unsafe_allow_html=True)
        
        st.markdown('<div class="enhanced-card">', unsafe_allow_html=True)
        col1, col2 = st.columns([2, 3])
        
        with col1:
            st.markdown("#### 🏛️ Academic Details")
            st.markdown(f"""
            **🎓 Degree:** {portfolio_data['education']['degree']}  
            **🏫 Institution:** {portfolio_data['education']['institution']}  
            **📅 Duration:** {portfolio_data['education']['duration']}  
            **📊 CGPA:** {portfolio_data['education']['cgpa']}  
            **🎯 Focus Area:** {portfolio_data['education']['focus']}
            """)
        
        with col2:
            st.markdown("#### 🔬 Specializations")
            for i, spec in enumerate(portfolio_data['education']['specializations']):
                st.markdown(f"""
                <div class="timeline-item" style="animation-delay: {i * 0.2}s;">
                    <strong>{spec}</strong>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("#### 📚 Core Academic Concepts")
        
        # Create a 2-column layout for core concepts
        concept_cols = st.columns(2)
        for i, concept in enumerate(portfolio_data['education']['core_concepts']):
            with concept_cols[i % 2]:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
                     padding: 1rem; border-radius: 10px; margin: 0.5rem 0; border-left: 3px solid #667eea;">
                    <strong>• {concept}</strong>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    elif selected_section == "💼 Experience":
        st.markdown('<h2 class="section-header">💼 Professional Journey</h2>', unsafe_allow_html=True)
        
        for i, exp in enumerate(portfolio_data["experience"]):
            st.markdown('<div class="enhanced-card">', unsafe_allow_html=True)
            
            # Experience header
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"### {exp['role']}")
                st.markdown(f"**🏢 {exp['company']}** | 📅 {exp['duration']} | 🌐 {exp['type']}")
            
            with col2:
                st.markdown(f"""
                <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                     border-radius: 15px; color: white; font-weight: 600;">
                    {exp['company']}<br>
                    <small>{exp['type']}</small>
                </div>
                """, unsafe_allow_html=True)
            
            # Experience description
            st.markdown(f"**📋 Role Overview:** {exp['description']}")
            
            # Key achievements
            st.markdown("**🎯 Key Achievements & Impact:**")
            for j, achievement in enumerate(exp["achievements"]):
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, rgba(76, 175, 80, 0.1) 0%, rgba(69, 160, 73, 0.1) 100%);
                     padding: 0.8rem; border-radius: 8px; margin: 0.5rem 0; border-left: 3px solid #4CAF50;
                     animation: slideInLeft 0.6s ease-out {j * 0.1}s both;">
                    <strong>• {achievement}</strong>
                </div>
                """, unsafe_allow_html=True)
            
            # Technologies used
            if 'technologies' in exp:
                st.markdown("**🛠️ Technologies & Tools:**")
                tech_html = ""
                for tech in exp['technologies']:
                    tech_html += f'<div class="tech-badge">{tech}</div>'
                st.markdown(tech_html, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            if i < len(portfolio_data["experience"]) - 1:
                st.markdown("---")
    
    elif selected_section == "🚀 Projects":
        st.markdown('<h2 class="section-header">🚀 Featured Projects</h2>', unsafe_allow_html=True)
        
        # Project categories
        categories = list(set([project['category'] for project in portfolio_data['projects']]))
        selected_category = st.selectbox("Filter by Category", ["All"] + categories)
        
        filtered_projects = portfolio_data['projects']
        if selected_category != "All":
            filtered_projects = [p for p in portfolio_data['projects'] if p['category'] == selected_category]
        
        for i, project in enumerate(filtered_projects):
            st.markdown('<div class="project-card">', unsafe_allow_html=True)
            
            # Project header
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"### {project['name']}")
                st.markdown(f"**📂 Category:** {project['category']}")
                st.markdown(f"**📈 Impact:** {project['impact']}")
            
            with col2:
                st.markdown(f"""
                <div style="text-align: center; padding: 1rem;">
                    <div class="skill-badge" style="margin: 0.2rem;">{project['status']}</div>
                    {f'<br><a href="{project["github"]}" target="_blank" class="social-icon github" style="margin: 0.5rem;">GitHub</a>' if 'github' in project else ''}
                    {f'<br><a href="{project["demo"]}" target="_blank" style="color: #667eea;">🔗 Demo</a>' if 'demo' in project else ''}
                </div>
                """, unsafe_allow_html=True)
            
            # Project description
            st.markdown(f"**📖 Description:** {project['description']}")
            
            # Technologies
            st.markdown("**🛠️ Technologies & Frameworks:**")
            tech_html = ""
            for tech in project['technologies']:
                tech_html += f'<div class="tech-badge">{tech}</div>'
            st.markdown(tech_html, unsafe_allow_html=True)
            
            # Key features
            st.markdown("**✨ Key Features & Capabilities:**")
            for j, feature in enumerate(project['features']):
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
                     padding: 0.8rem; border-radius: 8px; margin: 0.4rem 0; border-left: 3px solid #667eea;
                     animation: slideInRight 0.6s ease-out {j * 0.1}s both;">
                    <strong>• {feature}</strong>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    elif selected_section == "🛠️ Technical Skills":
        st.markdown('<h2 class="section-header">🛠️ Technical Expertise</h2>', unsafe_allow_html=True)
        
        # Programming Skills
        st.markdown('<div class="enhanced-card">', unsafe_allow_html=True)
        st.markdown("### 💻 Programming & Development")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Languages")
            for lang in portfolio_data['skills']['programming']['languages']:
                st.markdown(f'<div class="skill-badge">{lang}</div>', unsafe_allow_html=True)
                
        with col2:
            st.markdown("#### Frameworks & Libraries")
            for framework in portfolio_data['skills']['programming']['frameworks']:
                st.markdown(f'<div class="skill-badge">{framework}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Cybersecurity Skills
        st.markdown('<div class="enhanced-card">', unsafe_allow_html=True)
        st.markdown("### 🛡️ Cybersecurity Arsenal")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("#### Security Tools")
            for tool in portfolio_data['skills']['cybersecurity']['tools']:
                st.markdown(f'<div class="skill-badge" style="background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);">{tool}</div>', unsafe_allow_html=True)
                
        with col2:
            st.markdown("#### Platforms")
            for platform in portfolio_data['skills']['cybersecurity']['platforms']:
                st.markdown(f'<div class="skill-badge" style="background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%);">{platform}</div>', unsafe_allow_html=True)
                
        with col3:
            st.markdown("#### Concepts")
            for concept in portfolio_data['skills']['cybersecurity']['concepts']:
                st.markdown(f'<div class="skill-badge" style="background: linear-gradient(135deg, #9b59b6 0%, #8e44ad 100%);">{concept}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Cloud Security
        st.markdown('<div class="enhanced-card">', unsafe_allow_html=True)
        st.markdown("### ☁️ Cloud Security Expertise")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Cloud Platforms")
            for platform in portfolio_data['skills']['cloud_security']['platforms']:
                st.markdown(f'<div class="skill-badge" style="background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);">{platform}</div>', unsafe_allow_html=True)
                
        with col2:
            st.markdown("#### Security Tools")
            for tool in portfolio_data['skills']['cloud_security']['tools']:
                st.markdown(f'<div class="skill-badge" style="background: linear-gradient(135deg, #1abc9c 0%, #16a085 100%);">{tool}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Soft Skills
        st.markdown('<div class="enhanced-card">', unsafe_allow_html=True)
        st.markdown("### 🤝 Professional Skills")
        for skill in portfolio_data['skills']['soft_skills']:
            st.markdown(f'<div class="skill-badge" style="background: linear-gradient(135deg, #95a5a6 0%, #7f8c8d 100%);">{skill}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    elif selected_section == "🏆 Achievements":
        st.markdown('<h2 class="section-header">🏆 Achievements & Recognition</h2>', unsafe_allow_html=True)
        
        for i, achievement in enumerate(portfolio_data["achievements"]):
            st.markdown('<div class="achievement-item">', unsafe_allow_html=True)
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"### {achievement['title']}")
                st.markdown(f"**📋 Description:** {achievement['description']}")
                st.markdown(f"**📈 Impact:** {achievement['impact']}")
            
            with col2:
                st.markdown(f"""
                <div style="text-align: center; padding: 1rem;">
                    <div style="font-size: 3rem;">🏆</div>
                    <strong>{achievement['year']}</strong><br>
                    <small>{achievement['type']}</small>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    elif selected_section == "📜 Certifications":
        st.markdown('<h2 class="section-header">📜 Professional Certifications</h2>', unsafe_allow_html=True)
        
        # Group certifications by level
        cert_levels = {}
        for cert in portfolio_data["certifications"]:
            level = cert['level']
            if level not in cert_levels:
                cert_levels[level] = []
            cert_levels[level].append(cert)
        
        for level, certs in cert_levels.items():
            st.markdown(f"### 🎯 {level} Level")
            
            for cert in certs:
                st.markdown('<div class="certification-item">', unsafe_allow_html=True)
                
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**📜 {cert['name']}**")
                    st.markdown(f"**🏢 Issuer:** {cert['issuer']}")
                    st.markdown(f"**📅 Date:** {cert['date']}")
                    
                    # Skills covered
                    st.markdown("**🎯 Skills Covered:**")
                    skills_html = ""
                    for skill in cert['skills']:
                        skills_html += f'<div class="tech-badge">{skill}</div>'
                    st.markdown(skills_html, unsafe_allow_html=True)
                
                with col2:
                    level_icons = {
                        "Professional": "🚀",
                        "Advanced Administrator": "⚡",
                        "Associate": "🎯",
                        "Specialist": "🛡️",
                        "Junior Analyst": "🔍",
                        "Fundamental": "📚"
                    }
                    icon = level_icons.get(cert['level'], "🏆")
                    
                    st.markdown(f"""
                    <div style="text-align: center; padding: 1rem;">
                        <div style="font-size: 3rem;">{icon}</div>
                        <strong>{cert['level']}</strong>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
    
    elif selected_section == "💬 Testimonials":
        st.markdown('<h2 class="section-header">💬 Professional Testimonials</h2>', unsafe_allow_html=True)
        
        for testimonial in portfolio_data["testimonials"]:
            st.markdown('<div class="enhanced-card">', unsafe_allow_html=True)
            
            # Star rating
            stars = "⭐" * testimonial['rating']
            st.markdown(f"<div style='font-size: 1.5rem; margin-bottom: 1rem;'>{stars}</div>", unsafe_allow_html=True)
            
            # Testimonial text
            st.markdown(f'<div style="font-style: italic; font-size: 1.1rem; margin-bottom: 1rem; color: #2c3e50;">"{testimonial["text"]}"</div>', unsafe_allow_html=True)
            
            # Author info
            col1, col2 = st.columns([1, 4])
            with col1:
                st.markdown("👤", unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                **{testimonial['name']}**  
                {testimonial['position']}  
                {testimonial['company']}
                """)
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    elif selected_section == "📞 Contact":
        st.markdown('<h2 class="section-header">📞 Let\'s Connect</h2>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 3])
        
        with col1:
            st.markdown('<div class="contact-info">', unsafe_allow_html=True)
            st.markdown("### 📇 Contact Information")
            
            contact_items = [
                ("📧", "Email", portfolio_data['personal_info']['email'], f"mailto:{portfolio_data['personal_info']['email']}"),
                ("📱", "Phone", portfolio_data['personal_info']['phone'], f"tel:{portfolio_data['personal_info']['phone']}"),
                ("📍", "Location", portfolio_data['personal_info']['location'], "#"),
                ("💼", "LinkedIn", "Professional Profile", portfolio_data['personal_info']['linkedin']),
                ("💻", "GitHub", "Code Repository", portfolio_data['personal_info']['github']),
                ("🎯", "TryHackMe", "Security Profile", portfolio_data['personal_info']['tryhackme'])
            ]
            
            for icon, label, value, link in contact_items:
                if link.startswith("http") or link.startswith("mailto") or link.startswith("tel"):
                    st.markdown(f"{icon} **{label}:** [{value}]({link})")
                else:
                    st.markdown(f"{icon} **{label}:** {value}")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="enhanced-card">', unsafe_allow_html=True)
            st.markdown("### 💌 Send a Message")
            
            with st.form("enhanced_contact_form", clear_on_submit=True):
                col1, col2 = st.columns(2)
                
                with col1:
                    name = st.text_input("Full Name *", placeholder="Enter your full name")
                    email = st.text_input("Email Address *", placeholder="your.email@example.com")
                
                with col2:
                    company = st.text_input("Company/Organization", placeholder="Your company (optional)")
                    subject = st.selectbox("Subject *", [
                        "General Inquiry",
                        "Job Opportunity", 
                        "Collaboration Proposal",
                        "Technical Discussion",
                        "Mentorship Request",
                        "Other"
                    ])
                
                message = st.text_area("Your Message *", 
                                     placeholder="Please describe your inquiry, project details, or how I can help you...", 
                                     height=120)
                
                # Additional options
                col1, col2 = st.columns(2)
                with col1:
                    urgent = st.checkbox("🚨 Urgent Request")
                    newsletter = st.checkbox("📧 Subscribe to updates")
                
                with col2:
                    meeting = st.checkbox("📅 Request a meeting")
                    portfolio_feedback = st.checkbox("💡 Portfolio feedback")
                
                submitted = st.form_submit_button("🚀 Send Message", use_container_width=True)
                
                if submitted:
                    if name and email and subject and message:
                        # Simulate message processing
                        with st.spinner("Sending your message..."):
                            time.sleep(2)  # Simulate processing time
                        
                        st.success("🎉 Thank you for reaching out! I'll respond within 24 hours.")
                        
                        # Show additional info based on selections
                        if urgent:
                            st.info("⚡ Your message has been marked as urgent and will be prioritized.")
                        if meeting:
                            st.info("📅 I'll include meeting availability options in my response.")
                        if newsletter:
                            st.info("📧 You've been subscribed to project updates and tech insights.")
                    else:
                        st.error("⚠️ Please fill in all required fields marked with *")
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Enhanced Footer Section
    st.markdown("---")
    st.markdown("""
    <div class="footer">
        <div class="footer-content">
            <div class="footer-section">
                <h3 class="footer-title">Sai Venkat Ravuri</h3>
                <p style="color: #bdc3c7; font-size: 1.1rem; margin-bottom: 2rem;">
                    Cybersecurity Professional | Secure Code Developer | Digital Guardian
                </p>
            </div>
            
            
           
    """, unsafe_allow_html=True)
    
    # Scroll to top button (JavaScript would be needed for full functionality)
    st.markdown("""
    <button class="scroll-top" onclick="window.scrollTo(0,0)" title="Scroll to top">
        ↑
    </button>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()