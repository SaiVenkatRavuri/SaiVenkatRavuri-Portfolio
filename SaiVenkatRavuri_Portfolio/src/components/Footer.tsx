
import { Github, Linkedin, Heart } from 'lucide-react';

const Footer = () => {
  return (
    <footer className="bg-gradient-to-b from-slate-900/80 to-slate-900 border-t border-slate-700/50 py-16 backdrop-blur-sm">
      <div className="container mx-auto px-6">
        <div className="flex flex-col md:flex-row justify-between items-center mb-8">
          <div className="mb-8 md:mb-0 text-center md:text-left">
            <h3 className="text-2xl font-black text-white mb-3 bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
              Sai Venkat Ravuri
            </h3>
            <p className="text-slate-400 text-lg font-medium">IT Student & Aspiring Technical Support Engineer</p>
          </div>
          
          <div className="flex space-x-6">
            <a 
              href="https://github.com/22kq1a1259"
              target="_blank"
              rel="noopener noreferrer"
              className="w-14 h-14 bg-slate-800/50 hover:bg-purple-600/20 rounded-full flex items-center justify-center text-slate-400 hover:text-purple-400 transition-all duration-300 hover:scale-110 backdrop-blur-sm border border-slate-700/50 hover:border-purple-500/50 shadow-lg hover:shadow-purple-500/20"
            >
              <Github className="h-7 w-7" />
            </a>
            <a 
              href="https://linkedin.com/in/sai-venkat-ravuri-1143952b1"
              target="_blank"
              rel="noopener noreferrer"
              className="w-14 h-14 bg-slate-800/50 hover:bg-blue-600/20 rounded-full flex items-center justify-center text-slate-400 hover:text-blue-400 transition-all duration-300 hover:scale-110 backdrop-blur-sm border border-slate-700/50 hover:border-blue-500/50 shadow-lg hover:shadow-blue-500/20"
            >
              <Linkedin className="h-7 w-7" />
            </a>
          </div>
        </div>
        
        <div className="pt-8 border-t border-slate-700/50 text-center">
          <p className="text-slate-400 flex items-center justify-center text-lg font-medium">
            Crafted with 
            <Heart className="h-6 w-6 text-red-500 mx-3 animate-pulse" />
            by 
            <span className="ml-2 bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent font-semibold">
              Sai Venkat Ravuri
            </span>
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
