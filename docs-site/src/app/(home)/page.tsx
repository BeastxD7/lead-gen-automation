import Link from 'next/link';
import { ArrowRight, Brain, Map, Share, Download, Radar, Check } from 'lucide-react';

// Hero Section - Minimalist Design with Light/Dark Support
function HeroSection() {
  return (
    <section className="relative w-full bg-dark-bg dark:bg-[#0B0B0E] bg-white text-white dark:text-white overflow-hidden flex flex-col items-center pt-32 pb-24">
      {/* Background Effects */}
      <div className="absolute inset-0 grid-bg opacity-30 pointer-events-none" />
      <div className="absolute top-[-20%] left-1/2 -translate-x-1/2 w-[800px] h-[800px] bg-indigo-600/10 dark:bg-indigo-600/10 rounded-full blur-[150px] pointer-events-none" />

      <div className="container mx-auto px-6 relative z-10 flex flex-col items-center text-center">
        <div className="max-w-5xl mx-auto space-y-8">
          {/* Status Badge */}
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/[0.03] dark:bg-white/[0.03] bg-black/[0.03] border border-white/10 dark:border-white/10 border-black/10 backdrop-blur-md mb-6">
            <span className="w-1.5 h-1.5 rounded-full bg-violet-500 animate-pulse" />
            <span className="text-[11px] font-semibold text-indigo-300 dark:text-indigo-300 text-indigo-600 tracking-[0.15em] uppercase">
              The New Standard in Data
            </span>
          </div>

          {/* Main Title */}
          <h1 className="text-6xl md:text-8xl font-medium tracking-tight leading-[1.05] text-glow relative z-10">
            <span className="text-slate-900 dark:text-white">Quiet Precision.</span>
            <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-slate-400 dark:from-slate-200 to-slate-600 dark:to-slate-500">
              Infinite Scale.
            </span>
          </h1>

          <p className="text-lg md:text-xl text-slate-500 dark:text-slate-400 max-w-2xl mx-auto leading-relaxed font-light">
            Anvesh automates lead discovery through deep-web intelligence. Sophisticated scraping, simplified for global teams.
          </p>

          {/* CTA Button */}
          <div className="flex flex-col sm:flex-row items-center justify-center gap-6 pt-6">
            <Link
              href="/docs"
              className="px-10 py-4 bg-slate-900 dark:bg-white text-white dark:text-black rounded-full font-semibold hover:bg-slate-800 dark:hover:bg-indigo-50 transition-all shadow-glow flex items-center gap-2"
            >
              Start Discovery
              <ArrowRight className="w-5 h-5" />
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}

// Stats Section
function StatsSection() {
  return (
    <section className="relative z-20 -mt-10 mb-24">
      <div className="container mx-auto px-6 max-w-6xl">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <StatCard value="$0" label="Cost for Life" description="Open source core available for everyone forever." />
          <StatCard value="99.8%" label="Data Precision" description="Verified against multiple trusted sources." highlight />
          <StatCard value="1M+" label="Leads Scraped" description="Processed daily by our global node network." />
        </div>
      </div>
    </section>
  );
}

function StatCard({ value, label, description, highlight = false }: { value: string; label: string; description: string; highlight?: boolean }) {
  return (
    <div className={`stat-card ${highlight ? 'ring-1 ring-indigo-500/20 dark:bg-[#16161A] bg-indigo-50' : ''}`}>
      {highlight && <div className="absolute inset-0 bg-gradient-to-b from-indigo-500/5 to-transparent pointer-events-none" />}
      <h3 className="text-4xl md:text-5xl font-semibold text-slate-900 dark:text-white mb-2 tracking-tight">{value}</h3>
      <p className={`text-sm font-medium uppercase tracking-wider ${highlight ? 'text-indigo-600 dark:text-indigo-300' : 'text-slate-500'}`}>
        {label}
      </p>
      <p className="text-xs text-slate-500 dark:text-slate-600 mt-2 text-center max-w-[150px]">{description}</p>
    </div>
  );
}

// Why Choose Section
function WhyChooseSection() {
  return (
    <section className="py-24 bg-white dark:bg-[#0B0B0E] relative">
      <div className="container mx-auto px-6 max-w-6xl">
        <div className="flex flex-col lg:flex-row gap-16 items-center">
          <div className="lg:w-1/2">
            <h2 className="text-4xl md:text-5xl font-medium text-slate-900 dark:text-white leading-tight tracking-tight mb-6">
              Why choose <br />Anvesh?
            </h2>
            <p className="text-lg text-slate-500 font-light mb-8">
              We replace manual research with autonomous agents. Stop hunting for leads and start closing them.
            </p>
            <div className="grid grid-cols-1 gap-8">
              <FeatureItem
                icon={<Brain className="w-5 h-5" />}
                title="Deep-Web Intelligence"
                description="Access data layers invisible to standard search engines."
              />
              <FeatureItem
                icon={<Map className="w-5 h-5" />}
                title="Google Maps Scraping"
                description="Pinpoint local businesses with geographic precision."
              />
              <FeatureItem
                icon={<Share className="w-5 h-5" />}
                title="One-Click CSV Export"
                description="Instant compatibility with your CRM of choice."
              />
            </div>
          </div>

          <div className="lg:w-1/2 relative">
            <div className="relative w-full aspect-square max-w-md mx-auto">
              <div className="absolute inset-0 bg-gradient-to-tr from-indigo-500/10 to-purple-500/5 rounded-full blur-3xl" />
              <div className="relative z-10 w-full h-full border border-slate-200 dark:border-white/[0.05] rounded-3xl bg-slate-50 dark:bg-[#0E0E11] p-2 shadow-2xl overflow-hidden">
                {/* Animated rings */}
                <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 h-64 border border-indigo-500/20 rounded-full animate-spin" style={{ animationDuration: '10s' }} />
                <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-48 h-48 border border-dashed border-indigo-400/30 rounded-full animate-spin" style={{ animationDuration: '15s', animationDirection: 'reverse' }} />

                {/* Nodes */}
                <div className="absolute top-[30%] left-[20%] w-3 h-3 bg-indigo-500 rounded-full shadow-[0_0_15px_rgba(99,102,241,1)]" />
                <div className="absolute bottom-[40%] right-[25%] w-2 h-2 bg-purple-500 rounded-full shadow-[0_0_15px_rgba(168,85,247,1)]" />
                <div className="absolute top-[60%] left-[70%] w-2 h-2 bg-white rounded-full shadow-[0_0_10px_rgba(255,255,255,0.8)]" />

                {/* Status Card */}
                <div className="absolute bottom-6 left-6 right-6 p-4 glass-panel rounded-xl">
                  <div className="flex items-center gap-3">
                    <div className="w-8 h-8 rounded-full bg-indigo-500/20 flex items-center justify-center text-indigo-400">
                      <Check className="w-4 h-4" />
                    </div>
                    <div>
                      <p className="text-xs text-slate-900 dark:text-white font-medium">Extraction Complete</p>
                      <p className="text-[10px] text-slate-500">2,402 leads processed in 12s</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function FeatureItem({ icon, title, description }: { icon: React.ReactNode; title: string; description: string }) {
  return (
    <div className="flex gap-4 group">
      <div className="w-12 h-12 rounded-2xl bg-slate-100 dark:bg-[#1A1A1E] border border-slate-200 dark:border-white/10 flex items-center justify-center text-indigo-500 dark:text-indigo-400 group-hover:scale-110 transition-transform">
        {icon}
      </div>
      <div>
        <h4 className="text-slate-900 dark:text-white font-medium text-lg">{title}</h4>
        <p className="text-slate-500 text-sm mt-1 font-light">{description}</p>
      </div>
    </div>
  );
}

// How It Works Section
function HowItWorksSection() {
  return (
    <section className="py-24 bg-slate-50 dark:bg-[#0B0B0E] border-t border-slate-200 dark:border-white/[0.03]">
      <div className="container mx-auto px-6 max-w-6xl">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-medium text-slate-900 dark:text-white mb-4">How Anvesh Works</h2>
          <p className="text-slate-500 max-w-2xl mx-auto">From query to qualified leads in three simple steps.</p>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <StepCard
            step={1}
            title="Configure Target"
            description="Define your ideal customer profile using simple natural language parameters."
            preview={<div className="text-sm text-indigo-400 dark:text-indigo-300 font-mono">&quot;Bakeries in Canada&quot;</div>}
          />
          <StepCard
            step={2}
            title="Automated Hunt"
            description="Our intelligent nodes scan verify data points across multiple trusted sources."
            preview={
              <div className="flex items-center justify-center gap-1">
                <span className="w-1 h-4 bg-indigo-500/50 rounded-full animate-pulse" />
                <span className="w-1 h-6 bg-indigo-500/80 rounded-full animate-pulse" style={{ animationDelay: '0.1s' }} />
                <span className="w-1 h-3 bg-indigo-500/40 rounded-full animate-pulse" style={{ animationDelay: '0.2s' }} />
                <span className="text-xs text-slate-500 ml-2">Scanning...</span>
              </div>
            }
          />
          <StepCard
            step={3}
            title="Export Leads"
            description="Download verified contact information instantly ready for your outreach campaigns."
            preview={
              <div className="flex items-center justify-between w-full">
                <div className="flex items-center gap-2">
                  <Download className="w-4 h-4 text-green-500" />
                  <span className="text-sm text-slate-600 dark:text-slate-300">leads_export.csv</span>
                </div>
                <Download className="w-4 h-4 text-slate-400" />
              </div>
            }
          />
        </div>
      </div>
    </section>
  );
}

function StepCard({ step, title, description, preview }: { step: number; title: string; description: string; preview: React.ReactNode }) {
  return (
    <div className="glass-card-dark p-8 rounded-[2rem] relative group hover:border-indigo-500/30 transition-colors">
      <div className="w-10 h-10 rounded-full bg-slate-100 dark:bg-[#1A1A1E] border border-slate-200 dark:border-white/10 flex items-center justify-center text-slate-900 dark:text-white font-bold mb-6 group-hover:bg-indigo-600 group-hover:text-white transition-colors">
        {step}
      </div>
      <h3 className="text-xl font-medium text-slate-900 dark:text-white mb-3">{title}</h3>
      <p className="text-sm text-slate-500 leading-relaxed mb-6">{description}</p>
      <div className="bg-slate-100 dark:bg-[#0A0A0C] border border-slate-200 dark:border-white/5 rounded-xl p-3 min-h-[58px] flex items-center">
        {preview}
      </div>
    </div>
  );
}

// Developer Section
function DeveloperSection() {
  return (
    <section className="py-32 bg-white dark:bg-[#0B0B0E] relative overflow-hidden">
      <div className="container mx-auto px-6 max-w-4xl relative z-10 flex flex-col items-center">
        <div className="mb-16 text-center">
          <h2 className="text-3xl font-medium text-slate-900 dark:text-white tracking-tight mb-2">Built for Developers</h2>
          <p className="text-slate-500">Integrate our intelligence directly into your product.</p>
        </div>

        <div className="w-full bg-slate-100 dark:bg-[#101013] rounded-[2rem] border border-slate-200 dark:border-white/[0.05] overflow-hidden shadow-2xl relative">
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[80%] h-[80%] bg-indigo-500/5 blur-3xl pointer-events-none" />
          <div className="p-8 md:p-12 overflow-x-auto relative z-10">
            <div className="flex gap-2 mb-6 opacity-30">
              <div className="w-3 h-3 rounded-full bg-slate-400 dark:bg-white/20" />
              <div className="w-3 h-3 rounded-full bg-slate-400 dark:bg-white/20" />
              <div className="w-3 h-3 rounded-full bg-slate-400 dark:bg-white/20" />
            </div>
            <pre className="font-mono text-sm md:text-base leading-loose text-slate-600 dark:text-slate-400">
              <span className="text-slate-400 dark:text-slate-600 select-none">$ </span>
              <span className="text-indigo-600 dark:text-indigo-400">curl</span> -X POST https://api.anvesh.ai/v1/automation \{'\n'}
              {'  '}-H <span className="text-teal-600 dark:text-teal-400">&quot;Authorization: Bearer sk_live_...&quot;</span> \{'\n'}
              {'  '}-d <span className="text-slate-700 dark:text-slate-300">{`'{
    `}<span className="text-purple-600 dark:text-purple-300">&quot;target&quot;</span>: <span className="text-teal-600 dark:text-teal-300">&quot;marketing-agencies&quot;</span>{`,
    `}<span className="text-purple-600 dark:text-purple-300">&quot;location&quot;</span>: <span className="text-teal-600 dark:text-teal-300">&quot;NY&quot;</span>{`,
    `}<span className="text-purple-600 dark:text-purple-300">&quot;filters&quot;</span>{`: { `}<span className="text-teal-600 dark:text-teal-300">&quot;min_employees&quot;</span>{`: 10 }
  }'`}</span>{'\n'}
              <span className="text-slate-400 dark:text-slate-600 select-none">// Response</span>{'\n'}
              <span className="text-slate-700 dark:text-slate-300">{'{'}</span>{'\n'}
              {'  '}<span className="text-purple-600 dark:text-purple-300">&quot;status&quot;</span>: <span className="text-teal-600 dark:text-teal-300">&quot;success&quot;</span>,{'\n'}
              {'  '}<span className="text-purple-600 dark:text-purple-300">&quot;job_id&quot;</span>: <span className="text-teal-600 dark:text-teal-300">&quot;job_8f92a3...&quot;</span>,{'\n'}
              {'  '}<span className="text-purple-600 dark:text-purple-300">&quot;leads_found&quot;</span>: <span className="text-teal-600 dark:text-teal-300">1450</span>{'\n'}
              <span className="text-slate-700 dark:text-slate-300">{'}'}</span>
            </pre>
          </div>
        </div>

        <div className="mt-12">
          <Link
            href="/docs"
            className="text-xs uppercase tracking-[0.2em] font-semibold text-slate-500 hover:text-indigo-600 dark:hover:text-white transition-colors border-b border-transparent hover:border-indigo-500 pb-1"
          >
            Read Documentation
          </Link>
        </div>
      </div>
    </section>
  );
}

// Footer
function Footer() {
  return (
    <footer className="bg-slate-50 dark:bg-[#0B0B0E] text-slate-500 dark:text-slate-600 py-16 border-t border-slate-200 dark:border-white/[0.03]">
      <div className="container mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-8">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 bg-indigo-100 dark:bg-indigo-600/10 rounded-full flex items-center justify-center text-indigo-600 dark:text-indigo-400 border border-indigo-200 dark:border-indigo-500/20">
            <Radar className="w-4 h-4" />
          </div>
          <span className="text-lg font-medium text-slate-900 dark:text-white tracking-tight">Anvesh</span>
        </div>
        <div className="flex gap-8 text-[11px] uppercase tracking-widest font-semibold">
          <Link href="#" className="hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Privacy</Link>
          <Link href="#" className="hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Terms</Link>
          <Link href="#" className="hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">System</Link>
          <Link href="#" className="hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Support</Link>
        </div>
        <p className="text-[11px] uppercase tracking-widest font-medium opacity-50">© 2024</p>
      </div>
    </footer>
  );
}

// Main Page
export default function HomePage() {
  return (
    <main className="font-sans antialiased text-slate-600 dark:text-slate-400 bg-white dark:bg-[#0B0B0E] selection:bg-indigo-500/30 selection:text-white">
      <HeroSection />
      <StatsSection />
      <WhyChooseSection />
      <HowItWorksSection />
      <DeveloperSection />
      <Footer />
    </main>
  );
}
