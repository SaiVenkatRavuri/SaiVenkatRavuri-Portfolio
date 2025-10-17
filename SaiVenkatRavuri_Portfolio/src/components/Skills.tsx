
const Skills = () => {
  const skillCategories = [
    {
      title: "Programming Languages",
      skills: [
        { name: "C", level: 80 },
        { name: "Python", level: 85 },
        { name: "JavaScript", level: 75 }
      ],
      icon: "💻"
    },
    {
      title: "Web Technologies", 
      skills: [
        { name: "HTML", level: 90 },
        { name: "CSS", level: 85 },
        { name: "Bootstrap", level: 80 }
      ],
      icon: "🌐"
    },
    {
      title: "Database & Tools",
      skills: [
        { name: "SQL", level: 75 },
        { name: "Git", level: 80 },
        { name: "VS Code", level: 90 },
        { name: "Linux", level: 70 }
      ],
      icon: "🛠️"
    },
    {
      title: "Cybersecurity",
      skills: [
        { name: "Kali Linux", level: 75 },
        { name: "Nmap", level: 70 },
        { name: "Wireshark", level: 65 },
        { name: "Burp Suite", level: 60 }
      ],
      icon: "🔐"
    },
    {
      title: "Other Skills",
      skills: [
        { name: "API Integration", level: 75 },
        { name: "Debugging", level: 80 },
        { name: "Version Control", level: 85 }
      ],
      icon: "⚙️"
    }
  ];

  return (
    <section id="skills" className="py-24 bg-gradient-to-b from-slate-800/60 to-slate-900/60 backdrop-blur-sm">
      <div className="container mx-auto px-6">
        <h2 className="text-5xl md:text-6xl font-black text-center mb-20 bg-gradient-to-r from-blue-400 via-cyan-400 to-purple-400 bg-clip-text text-transparent">
          Skills & Technologies
        </h2>
        
        <div className="max-w-7xl mx-auto">
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-10">
            {skillCategories.map((category, categoryIndex) => (
              <div 
                key={categoryIndex}
                className="group bg-gradient-to-br from-slate-700/40 to-slate-800/40 p-8 rounded-3xl border border-slate-600/40 hover:border-blue-500/60 transition-all duration-500 hover:scale-105 backdrop-blur-sm shadow-xl hover:shadow-2xl hover:shadow-blue-500/20 hover:from-slate-700/60 hover:to-slate-800/60"
              >
                <div className="text-center mb-8">
                  <div className="text-4xl mb-4 group-hover:scale-110 transition-transform duration-300">
                    {category.icon}
                  </div>
                  <h3 className="text-2xl font-bold text-blue-400 group-hover:text-cyan-400 transition-colors duration-300">
                    {category.title}
                  </h3>
                </div>
                
                <div className="space-y-6">
                  {category.skills.map((skill, skillIndex) => (
                    <div key={skillIndex} className="space-y-3">
                      <div className="flex justify-between items-center">
                        <span className="text-white font-semibold text-lg">{skill.name}</span>
                        <span className="text-slate-400 text-sm font-medium bg-slate-600/30 px-3 py-1 rounded-full">
                          {skill.level}%
                        </span>
                      </div>
                      
                      <div className="w-full bg-slate-600/30 rounded-full h-3 overflow-hidden backdrop-blur-sm">
                        <div 
                          className="bg-gradient-to-r from-blue-500 via-cyan-500 to-blue-600 h-3 rounded-full transition-all duration-1000 ease-out shadow-lg shadow-blue-500/30 relative overflow-hidden"
                          style={{ width: `${skill.level}%` }}
                        >
                          <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent animate-pulse"></div>
                        </div>
                      </div>
                    </div>
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

export default Skills;
