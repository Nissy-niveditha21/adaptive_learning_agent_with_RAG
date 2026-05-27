export default function Hero({ onStartSession, loading }) {
    return (
        <section className="hero-card glass-card">
            <div className="hero-text-block">
                <div className="hero-copy">
                    <span className="eyebrow">AI Tutor for focused mastery</span>
                    <h1>Learn Smarter with AI</h1>
                    <p>
                        Personalized checkpoint-driven learning powered by RAG and LangGraph.
                        Train your understanding, surface weak areas, and lock in concepts with
                        intelligent tutoring.
                    </p>
                </div>

                <div className="hero-action">
                    <button
                        className="button button-primary"
                        onClick={onStartSession}
                        disabled={loading}
                    >
                        {loading ? 'Starting Session...' : 'Start Learning Session'}
                    </button>
                    <div className="hero-badge">
                        <strong>Ready for deployment</strong>
                        <span>Modern dark dashboard, AI-focused workflow, real-world SaaS feel.</span>
                    </div>
                </div>
            </div>

            <div className="hero-visual" aria-label="Learning agent visual preview">
                <img src="/learning-agent-hero.svg" alt="AI learning dashboard preview" />
            </div>
        </section>
    );
}
