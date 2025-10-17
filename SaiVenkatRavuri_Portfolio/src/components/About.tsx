
const About = () => {
  const strengths = [
    { 
      title: "Clear Communication", 
      description: "Excellent at explaining technical concepts",
      icon: "💬"
    },
    { 
      title: "Team Collaboration", 
      description: "Strong teamwork and interpersonal skills",
      icon: "🤝"
    },
    { 
      title: "Adaptability", 
      description: "Quick to learn new technologies and adapt",
      icon: "⚡"
    },
    { 
      title: "Self-Motivation", 
      description: "Proactive and driven by continuous learning",
      icon: "🎯"
    }
  ];

  return (
    <section id="about" className="py-24 bg-gradient-to-b from-slate-800/30 to-slate-800/60 backdrop-blur-sm">
      <div className="container mx-auto px-6">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-5xl md:text-6xl font-black text-center mb-20 bg-gradient-to-r from-blue-400 via-cyan-400 to-purple-400 bg-clip-text text-transparent">
            About Me
          </h2>
          
          <div className="grid lg:grid-cols-2 gap-16 items-center">
            <div className="space-y-8">
              <p className="text-xl text-slate-300 leading-relaxed font-medium">
                Motivated and technically skilled IT student seeking a Technical Support Engineer role. 
                Passionate about learning, problem-solving, and building practical solutions that make a difference.
              </p>
              
              <p className="text-xl text-slate-300 leading-relaxed font-medium">
                With hands-on experience in Python development, web technologies, and cybersecurity tools, 
                I'm ready to contribute to dynamic tech teams while continuing to grow professionally.
              </p>

              <div className="pt-6">
                <div className="w-20 h-1 bg-gradient-to-r from-blue-400 to-cyan-400 rounded-full"></div>
              </div>
            </div>
            
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-8">
              {strengths.map((strength, index) => (
                <div 
                  key={index}
                  className="group bg-gradient-to-br from-slate-700/40 to-slate-800/40 p-8 rounded-2xl hover:from-slate-700/60 hover:to-slate-800/60 transition-all duration-500 hover:scale-105 border border-slate-600/30 hover:border-blue-500/40 backdrop-blur-sm shadow-lg hover:shadow-xl hover:shadow-blue-500/20"
                >
                  <div className="text-3xl mb-4 group-hover:scale-110 transition-transform duration-300">
                    {strength.icon}
                  </div>
                  <h3 className="font-bold text-xl text-blue-400 mb-3 group-hover:text-cyan-400 transition-colors duration-300">
                    {strength.title}
                  </h3>
                  <p className="text-slate-400 leading-relaxed font-medium">
                    {strength.description}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;
