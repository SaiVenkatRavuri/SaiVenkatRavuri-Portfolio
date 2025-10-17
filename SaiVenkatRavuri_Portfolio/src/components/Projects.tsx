
import { ExternalLink, Github } from 'lucide-react';
import { Button } from '@/components/ui/button';

const Projects = () => {
  const projects = [
    {
      title: "Travel Website",
      description: "Responsive web application for transportation information with mobile-optimized UI",
      technologies: ["HTML", "CSS", "Bootstrap", "JavaScript"],
      features: [
        "Responsive design across all devices",
        "Transportation information system", 
        "Mobile-optimized user interface",
        "Modern Bootstrap 5 styling"
      ],
      image: "https://images.unsplash.com/photo-1500673922987-e212871fec22?w=600&h=400&fit=crop",
      status: "completed",
      icon: "🌍"
    }
  ];

  return (
    <section id="projects" className="py-24 bg-gradient-to-b from-slate-900/60 to-slate-800/60">
      <div className="container mx-auto px-6">
        <h2 className="text-5xl md:text-6xl font-black text-center mb-20 bg-gradient-to-r from-blue-400 via-cyan-400 to-purple-400 bg-clip-text text-transparent">
          Projects
        </h2>
        
        <div className="max-w-7xl mx-auto">
          <div className="grid lg:grid-cols-1 gap-12">
            {projects.map((project, index) => (
              <div 
                key={index}
                className="group bg-gradient-to-br from-slate-700/40 to-slate-800/40 rounded-3xl overflow-hidden border border-slate-600/40 hover:border-blue-500/60 transition-all duration-500 hover:scale-[1.02] backdrop-blur-sm shadow-xl hover:shadow-2xl hover:shadow-blue-500/20 hover:from-slate-700/60 hover:to-slate-800/60"
              >
                <div className="lg:flex">
                  <div className="lg:w-1/2 relative overflow-hidden">
                    <img 
                      src={project.image} 
                      alt={project.title}
                      className="w-full h-80 lg:h-full object-cover group-hover:scale-110 transition-transform duration-700"
                    />
                    <div className="absolute inset-0 bg-gradient-to-r from-blue-600/20 to-cyan-600/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                  </div>
                  
                  <div className="lg:w-1/2 p-10">
                    <div className="flex items-center gap-4 mb-6">
                      <div className="text-3xl group-hover:scale-110 transition-transform duration-300">
                        {project.icon}
                      </div>
                      <h3 className="text-3xl font-bold text-white group-hover:text-blue-300 transition-colors duration-300">
                        {project.title}
                      </h3>
                      <span className="px-4 py-2 bg-gradient-to-r from-green-500/20 to-emerald-500/20 text-green-400 text-sm font-semibold rounded-full border border-green-500/40 shadow-lg shadow-green-500/20">
                        Completed
                      </span>
                    </div>
                    
                    <p className="text-slate-300 mb-8 leading-relaxed text-lg font-medium">
                      {project.description}
                    </p>
                    
                    <div className="mb-8">
                      <h4 className="text-blue-400 font-bold text-lg mb-4 group-hover:text-cyan-400 transition-colors duration-300">
                        Key Features:
                      </h4>
                      <ul className="space-y-3">
                        {project.features.map((feature, featureIndex) => (
                          <li key={featureIndex} className="text-slate-300 flex items-center text-lg font-medium">
                            <div className="w-3 h-3 bg-gradient-to-r from-blue-400 to-cyan-400 rounded-full mr-4 group-hover:scale-125 transition-transform duration-300"></div>
                            {feature}
                          </li>
                        ))}
                      </ul>
                    </div>
                    
                    <div className="mb-8">
                      <div className="flex flex-wrap gap-3">
                        {project.technologies.map((tech, techIndex) => (
                          <span 
                            key={techIndex}
                            className="px-4 py-2 bg-gradient-to-r from-blue-500/10 to-cyan-500/10 text-blue-300 text-sm font-semibold rounded-full border border-blue-500/30 hover:border-blue-400/50 transition-all duration-300 hover:scale-105 backdrop-blur-sm"
                          >
                            {tech}
                          </span>
                        ))}
                      </div>
                    </div>
                    
                    <div className="flex gap-4">
                      <Button 
                        variant="outline" 
                        className="border-2 border-blue-400/60 text-blue-400 hover:bg-blue-400 hover:text-slate-900 transition-all duration-300 hover:scale-105 px-6 py-3 rounded-full font-semibold backdrop-blur-sm"
                      >
                        <ExternalLink className="mr-2 h-5 w-5" />
                        View Project
                      </Button>
                      <Button 
                        variant="outline" 
                        className="border-2 border-cyan-400/60 text-cyan-400 hover:bg-cyan-400 hover:text-slate-900 transition-all duration-300 hover:scale-105 px-6 py-3 rounded-full font-semibold backdrop-blur-sm"
                      >
                        <Github className="mr-2 h-5 w-5" />
                        View Code
                      </Button>
                    </div>
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

export default Projects;
