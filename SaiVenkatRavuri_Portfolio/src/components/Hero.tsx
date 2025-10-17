
import { Download, Github, Linkedin, ArrowDown } from 'lucide-react';
import { Button } from '@/components/ui/button';

const Hero = () => {
  return (
    <section id="home" className="min-h-screen flex items-center justify-center relative overflow-hidden pt-20">
      {/* Enhanced Animated Background */}
      <div className="absolute inset-0 bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
        <div className="absolute inset-0 bg-gradient-to-r from-blue-600/10 via-cyan-600/5 to-blue-600/10"></div>
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_20%_80%,_theme(colors.blue.600/15)_0%,_transparent_60%)]"></div>
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_80%_20%,_theme(colors.cyan.600/10)_0%,_transparent_60%)]"></div>
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_40%_40%,_theme(colors.purple.600/8)_0%,_transparent_60%)]"></div>
      </div>
      
      {/* Enhanced floating particles */}
      <div className="absolute inset-0 overflow-hidden">
        {[...Array(30)].map((_, i) => (
          <div
            key={i}
            className="absolute w-1 h-1 bg-gradient-to-r from-blue-400 to-cyan-400 rounded-full opacity-60"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
              animationDelay: `${Math.random() * 5}s`,
              animationDuration: `${3 + Math.random() * 4}s`,
              animation: 'pulse 3s ease-in-out infinite'
            }}
          ></div>
        ))}
      </div>

      <div className="container mx-auto px-6 relative z-10">
        <div className="max-w-7xl mx-auto">
          <div className="grid lg:grid-cols-2 gap-16 items-center">
            {/* Enhanced Left Content */}
            <div className="animate-fade-in space-y-8">
              {/* Status Badge */}
              <div className="mb-8">
                <span className="inline-flex items-center px-6 py-3 bg-gradient-to-r from-green-500/10 to-emerald-500/10 text-green-400 text-sm font-medium rounded-full border border-green-500/20 shadow-lg shadow-green-500/10">
                  <div className="w-2 h-2 bg-green-400 rounded-full mr-3 animate-pulse"></div>
                  Available for new opportunities
                </span>
              </div>

              {/* Enhanced Main Heading */}
              <div className="mb-10">
                <h1 className="text-7xl md:text-8xl lg:text-9xl font-black mb-8 leading-none">
                  <span className="block text-slate-100 tracking-tight">Hey,</span>
                  <span className="block text-slate-100 italic tracking-tight">there</span>
                </h1>
                
                <div className="mb-8">
                  <div className="text-5xl md:text-6xl lg:text-7xl font-black text-white mb-3 tracking-tight">
                    I AM
                  </div>
                  <div className="text-5xl md:text-6xl lg:text-7xl font-black bg-gradient-to-r from-blue-400 via-cyan-400 to-blue-500 bg-clip-text text-transparent mb-6 tracking-tight">
                    SAI VENKAT
                  </div>
                </div>

                <div className="space-y-2">
                  <div className="text-2xl md:text-3xl lg:text-4xl font-bold text-blue-400">
                    IT STUDENT &
                  </div>
                  <div className="text-2xl md:text-3xl lg:text-4xl font-bold text-cyan-400">
                    ASPIRING TECHNICAL
                  </div>
                  <div className="text-2xl md:text-3xl lg:text-4xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
                    SUPPORT ENGINEER
                  </div>
                </div>
              </div>

              <p className="text-xl text-slate-300 mb-10 max-w-xl leading-relaxed font-medium">
                Specialized in Web Development, Python Programming, and Network Security. 
                Building practical solutions with modern technologies.
              </p>

              {/* Enhanced Location */}
              <div className="flex items-center mb-10 text-slate-400">
                <div className="w-3 h-3 bg-gradient-to-r from-blue-400 to-cyan-400 rounded-full mr-3"></div>
                <span className="text-lg font-medium">Near Ongole, Andhra Pradesh, India</span>
              </div>

              {/* Enhanced CTA Buttons */}
              <div className="flex flex-col sm:flex-row gap-6 mb-12">
                <Button 
                  size="lg" 
                  className="bg-gradient-to-r from-blue-600 to-cyan-600 hover:from-blue-700 hover:to-cyan-700 text-white px-10 py-4 rounded-full transition-all duration-300 hover:scale-105 hover:shadow-xl hover:shadow-blue-500/30 text-lg font-semibold"
                >
                  <Download className="mr-3 h-6 w-6" />
                  Download Resume
                </Button>
                
                <Button 
                  variant="outline" 
                  size="lg" 
                  className="border-2 border-white/30 text-white hover:bg-white hover:text-slate-900 px-10 py-4 rounded-full transition-all duration-300 hover:scale-105 text-lg font-semibold backdrop-blur-sm"
                  onClick={() => window.open('https://github.com/22kq1a1259', '_blank')}
                >
                  <Github className="mr-3 h-6 w-6" />
                  View GitHub
                </Button>
              </div>

              {/* Enhanced Social Links */}
              <div className="flex space-x-8">
                <a 
                  href="https://github.com/22kq1a1259"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-14 h-14 bg-slate-800/50 hover:bg-blue-600/20 rounded-full flex items-center justify-center text-slate-400 hover:text-blue-400 transition-all duration-300 hover:scale-110 backdrop-blur-sm border border-slate-700/50 hover:border-blue-500/50"
                >
                  <Github className="h-7 w-7" />
                </a>
                <a 
                  href="https://linkedin.com/in/sai-venkat-ravuri-1143952b1"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-14 h-14 bg-slate-800/50 hover:bg-blue-600/20 rounded-full flex items-center justify-center text-slate-400 hover:text-blue-400 transition-all duration-300 hover:scale-110 backdrop-blur-sm border border-slate-700/50 hover:border-blue-500/50"
                >
                  <Linkedin className="h-7 w-7" />
                </a>
              </div>
            </div>

            {/* Enhanced Right Content with Circular Image */}
            <div className="flex justify-center lg:justify-end animate-scale-in">
              <div className="relative">
                <div className="w-96 h-96 lg:w-[28rem] lg:h-[28rem] rounded-full bg-gradient-to-br from-blue-500 via-cyan-500 to-purple-600 p-2 shadow-2xl shadow-blue-500/20">
                  <div className="w-full h-full rounded-full overflow-hidden border-4 border-slate-700/50">
                    <img 
                      src="https://i.postimg.cc/wjpkhh6z/Whats-App-Image-2025-06-23-at-13-42-52-ad64fb68.jpg"
                      alt="Sai Venkat Ravuri"
                      className="w-full h-full object-cover"
                    />
                  </div>
                </div>
                <div className="absolute -inset-6 rounded-full bg-gradient-to-r from-blue-500 via-cyan-500 to-purple-600 opacity-20 blur-2xl animate-pulse"></div>
                <div className="absolute -inset-8 rounded-full bg-gradient-to-r from-blue-600 to-cyan-600 opacity-10 blur-3xl animate-pulse" style={{ animationDelay: '1s' }}></div>
              </div>
            </div>
          </div>
        </div>

        {/* Enhanced scroll indicator */}
        <div className="absolute bottom-12 left-1/2 transform -translate-x-1/2 animate-bounce">
          <div className="w-8 h-12 border-2 border-blue-400/60 rounded-full flex justify-center backdrop-blur-sm">
            <ArrowDown className="h-4 w-4 text-blue-400 mt-2 animate-pulse" />
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
