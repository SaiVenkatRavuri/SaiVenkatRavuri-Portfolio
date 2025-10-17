
import { Mail, Phone, Linkedin, Github, MapPin, Send } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { useState } from 'react';

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('Form submitted:', formData);
    // Handle form submission logic here
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const contactInfo = [
    {
      icon: Mail,
      label: "Email",
      value: "ravurisaivenkat@gmail.com",
      href: "mailto:ravurisaivenkat@gmail.com",
      color: "from-red-500 to-pink-500"
    },
    {
      icon: Phone,
      label: "Phone", 
      value: "+91 63013 63267",
      href: "tel:+916301363267",
      color: "from-green-500 to-emerald-500"
    },
    {
      icon: Linkedin,
      label: "LinkedIn",
      value: "sai-venkat-ravuri",
      href: "https://linkedin.com/in/sai-venkat-ravuri-1143952b1",
      color: "from-blue-500 to-cyan-500"
    },
    {
      icon: Github,
      label: "GitHub",
      value: "22kq1a1259",
      href: "https://github.com/22kq1a1259",
      color: "from-purple-500 to-indigo-500"
    },
    {
      icon: MapPin,
      label: "Location",
      value: "Near Ongole, A.P, India",
      href: "#",
      color: "from-orange-500 to-red-500"
    }
  ];

  return (
    <section id="contact" className="py-24 bg-gradient-to-b from-slate-900/60 to-slate-800/60">
      <div className="container mx-auto px-6">
        <h2 className="text-5xl md:text-6xl font-black text-center mb-20 bg-gradient-to-r from-blue-400 via-cyan-400 to-purple-400 bg-clip-text text-transparent">
          Get In Touch
        </h2>
        
        <div className="max-w-7xl mx-auto">
          <div className="grid lg:grid-cols-2 gap-16">
            {/* Enhanced Contact Information */}
            <div className="space-y-10">
              <div>
                <h3 className="text-3xl font-bold text-white mb-6 bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
                  Contact Information
                </h3>
                <p className="text-xl text-slate-300 mb-10 leading-relaxed font-medium">
                  I'm always open to discussing new opportunities, collaborations, or just having a chat about technology. 
                  Feel free to reach out!
                </p>
                <div className="w-20 h-1 bg-gradient-to-r from-blue-400 to-cyan-400 rounded-full"></div>
              </div>
              
              <div className="space-y-6">
                {contactInfo.map((info, index) => (
                  <div key={index} className="group flex items-center space-x-6 p-4 rounded-2xl hover:bg-slate-700/30 transition-all duration-300">
                    <div className={`w-16 h-16 bg-gradient-to-r ${info.color} rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform duration-300 shadow-lg`}>
                      <info.icon className="h-8 w-8 text-white" />
                    </div>
                    <div>
                      <p className="text-slate-400 text-sm font-medium uppercase tracking-wide">{info.label}</p>
                      {info.href && info.href !== '#' ? (
                        <a 
                          href={info.href}
                          className="text-white hover:text-blue-400 transition-colors duration-300 text-lg font-semibold"
                          target={info.href.startsWith('http') ? '_blank' : undefined}
                          rel={info.href.startsWith('http') ? 'noopener noreferrer' : undefined}
                        >
                          {info.value}
                        </a>
                      ) : (
                        <span className="text-white text-lg font-semibold">{info.value}</span>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            </div>
            
            {/* Enhanced Contact Form */}
            <div className="bg-gradient-to-br from-slate-700/40 to-slate-800/40 p-10 rounded-3xl border border-slate-600/40 backdrop-blur-sm shadow-xl">
              <h3 className="text-3xl font-bold text-white mb-8 bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
                Send a Message
              </h3>
              
              <form onSubmit={handleSubmit} className="space-y-8">
                <div>
                  <Label htmlFor="name" className="text-slate-300 text-lg font-medium mb-3 block">Name</Label>
                  <Input
                    id="name"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    className="bg-slate-600/30 border-slate-500/50 text-white placeholder-slate-400 focus:border-blue-400 focus:ring-2 focus:ring-blue-400/20 h-14 text-lg rounded-xl backdrop-blur-sm"
                    placeholder="Your full name"
                    required
                  />
                </div>
                
                <div>
                  <Label htmlFor="email" className="text-slate-300 text-lg font-medium mb-3 block">Email</Label>
                  <Input
                    id="email"
                    name="email"
                    type="email"
                    value={formData.email}
                    onChange={handleChange}
                    className="bg-slate-600/30 border-slate-500/50 text-white placeholder-slate-400 focus:border-blue-400 focus:ring-2 focus:ring-blue-400/20 h-14 text-lg rounded-xl backdrop-blur-sm"
                    placeholder="your.email@example.com"
                    required
                  />
                </div>
                
                <div>
                  <Label htmlFor="message" className="text-slate-300 text-lg font-medium mb-3 block">Message</Label>
                  <textarea
                    id="message"
                    name="message"
                    value={formData.message}
                    onChange={handleChange}
                    rows={6}
                    className="w-full px-4 py-4 bg-slate-600/30 border border-slate-500/50 rounded-xl text-white placeholder-slate-400 focus:border-blue-400 focus:ring-2 focus:ring-blue-400/20 focus:outline-none resize-none text-lg backdrop-blur-sm"
                    placeholder="Your message here..."
                    required
                  />
                </div>
                
                <Button 
                  type="submit"
                  className="w-full bg-gradient-to-r from-blue-600 to-cyan-600 hover:from-blue-700 hover:to-cyan-700 text-white py-4 rounded-xl transition-all duration-300 hover:scale-105 text-lg font-semibold shadow-lg shadow-blue-500/30 hover:shadow-blue-500/50"
                >
                  <Send className="mr-3 h-6 w-6" />
                  Send Message
                </Button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Contact;
