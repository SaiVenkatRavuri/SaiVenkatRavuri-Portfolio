
const Experience = () => {
  const experiences = [
    {
      title: "AI Chatbot Developer",
      company: "Open Weaver",
      duration: "May 2025",
      type: "Project",
      description: "Built Python chatbot with logic trees and NLU",
      technologies: ["Python", "NLU", "Logic Trees"],
      status: "upcoming",
      icon: "🤖"
    },
    {
      title: "AI-ML Internship",
      company: "Google",
      duration: "Jan 2025 - Mar 2025",
      type: "Internship",
      description: "Developed ML models using Python, scikit-learn",
      technologies: ["Python", "scikit-learn", "Machine Learning"],
      status: "upcoming",
      icon: "🧠"
    },
    {
      title: "Network Security Associate Intern",
      company: "Fortinet",
      duration: "Dec 2024 - Jan 2025",
      type: "Internship",
      description: "Hands-on firewall/VPN/IDS/IPS configuration",
      technologies: ["Firewall", "VPN", "IDS/IPS", "Network Security"],
      status: "current",
      icon: "🔒"
    }
  ];

  return (
    <section id="experience" className="py-24 bg-gradient-to-b from-slate-800/60 to-slate-900/60 backdrop-blur-sm">
      <div className="container mx-auto px-6">
        <h2 className="text-5xl md:text-6xl font-black text-center mb-20 bg-gradient-to-r from-blue-400 via-cyan-400 to-purple-400 bg-clip-text text-transparent">
          Experience
        </h2>
        
        <div className="max-w-6xl mx-auto">
          <div className="grid gap-10">
            {experiences.map((exp, index) => (
              <div 
                key={index}
                className="group bg-gradient-to-br from-slate-700/40 to-slate-800/40 p-10 rounded-3xl border border-slate-600/40 hover:border-blue-500/60 transition-all duration-500 hover:scale-[1.02] backdrop-blur-sm shadow-xl hover:shadow-2xl hover:shadow-blue-500/20 hover:from-slate-700/60 hover:to-slate-800/60"
              >
                <div className="flex flex-col lg:flex-row lg:justify-between lg:items-start mb-6">
                  <div className="flex-1">
                    <div className="flex items-center gap-4 mb-4">
                      <div className="text-3xl group-hover:scale-110 transition-transform duration-300">
                        {exp.icon}
                      </div>
                      <h3 className="text-2xl font-bold text-white group-hover:text-blue-300 transition-colors duration-300">
                        {exp.title}
                      </h3>
                      {exp.status === 'current' && (
                        <span className="px-4 py-2 bg-gradient-to-r from-green-500/20 to-emerald-500/20 text-green-400 text-sm font-semibold rounded-full border border-green-500/40 shadow-lg shadow-green-500/20 animate-pulse">
                          Current
                        </span>
                      )}
                      {exp.status === 'upcoming' && (
                        <span className="px-4 py-2 bg-gradient-to-r from-blue-500/20 to-cyan-500/20 text-blue-400 text-sm font-semibold rounded-full border border-blue-500/40 shadow-lg shadow-blue-500/20">
                          Upcoming
                        </span>
                      )}
                    </div>
                    <p className="text-blue-400 font-bold text-xl group-hover:text-cyan-400 transition-colors duration-300">
                      {exp.company}
                    </p>
                    <p className="text-slate-400 mb-6 text-lg font-medium">
                      {exp.duration} • {exp.type}
                    </p>
                  </div>
                </div>
                
                <p className="text-slate-300 mb-6 leading-relaxed text-lg font-medium">
                  {exp.description}
                </p>
                
                <div className="flex flex-wrap gap-3">
                  {exp.technologies.map((tech, techIndex) => (
                    <span 
                      key={techIndex}
                      className="px-4 py-2 bg-gradient-to-r from-blue-500/10 to-cyan-500/10 text-blue-300 text-sm font-semibold rounded-full border border-blue-500/30 hover:border-blue-400/50 transition-all duration-300 hover:scale-105 backdrop-blur-sm"
                    >
                      {tech}
                    </span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Experience;
