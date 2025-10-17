
const Education = () => {
  const education = [
    {
      degree: "B.Tech in Information Technology",
      institution: "Pace Institute of Technology & Sciences",
      duration: "2022 - 2026",
      grade: "CGPA: 7.62/10",
      status: "current",
      icon: "🎓"
    },
    {
      degree: "Intermediate (MPC)",
      institution: "Viswa Bharathi Junior College",
      duration: "2020 - 2022",
      grade: "66%",
      status: "completed",
      icon: "📚"
    },
    {
      degree: "SSC",
      institution: "D.R.K.R High School",
      duration: "2019 - 2020",
      grade: "91%",
      status: "completed",
      icon: "🏫"
    }
  ];

  return (
    <section id="education" className="py-24 bg-gradient-to-b from-slate-900/50 to-slate-800/50">
      <div className="container mx-auto px-6">
        <h2 className="text-5xl md:text-6xl font-black text-center mb-20 bg-gradient-to-r from-blue-400 via-cyan-400 to-purple-400 bg-clip-text text-transparent">
          Education
        </h2>
        
        <div className="max-w-5xl mx-auto">
          <div className="relative">
            {/* Enhanced Timeline line */}
            <div className="absolute left-10 top-0 bottom-0 w-1 bg-gradient-to-b from-blue-500 via-cyan-500 to-blue-500 opacity-60"></div>
            
            {education.map((edu, index) => (
              <div key={index} className="relative pl-24 pb-16 last:pb-0 group">
                {/* Enhanced Timeline dot */}
                <div className={`absolute left-6 w-8 h-8 rounded-full border-4 flex items-center justify-center text-lg transition-all duration-500 group-hover:scale-125 ${
                  edu.status === 'current' 
                    ? 'bg-gradient-to-r from-blue-500 to-cyan-500 border-blue-400 shadow-lg shadow-blue-500/50 animate-pulse' 
                    : 'bg-gradient-to-r from-slate-700 to-slate-600 border-blue-500/60 hover:border-blue-400'
                }`}>
                  <span className="text-white text-sm">{edu.icon}</span>
                </div>
                
                <div className="bg-gradient-to-br from-slate-800/60 to-slate-700/60 p-8 rounded-2xl border border-slate-600/40 hover:border-blue-500/60 transition-all duration-500 hover:scale-[1.02] backdrop-blur-sm shadow-lg hover:shadow-xl hover:shadow-blue-500/20 group-hover:from-slate-800/80 group-hover:to-slate-700/80">
                  <div className="flex flex-col lg:flex-row lg:justify-between lg:items-start mb-4">
                    <h3 className="text-2xl font-bold text-white group-hover:text-blue-300 transition-colors duration-300">
                      {edu.degree}
                    </h3>
                    {edu.status === 'current' && (
                      <span className="inline-block px-4 py-2 bg-gradient-to-r from-blue-500/20 to-cyan-500/20 text-blue-400 text-sm font-semibold rounded-full border border-blue-500/40 shadow-lg shadow-blue-500/20 animate-pulse">
                        Current
                      </span>
                    )}
                  </div>
                  
                  <p className="text-blue-400 font-semibold text-lg mb-4 group-hover:text-cyan-400 transition-colors duration-300">
                    {edu.institution}
                  </p>
                  <div className="flex flex-col sm:flex-row sm:justify-between items-start sm:items-center">
                    <span className="text-slate-400 font-medium text-lg">{edu.duration}</span>
                    <span className="text-cyan-400 font-bold text-lg bg-gradient-to-r from-cyan-400 to-blue-400 bg-clip-text text-transparent">
                      {edu.grade}
                    </span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Education;
