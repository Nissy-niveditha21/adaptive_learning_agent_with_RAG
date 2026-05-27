export default function FeedbackCard({ semanticScore, status, weakAreas, retryCount }) {
    return (
        <section className="panel-card feedback-card glass-card">
            <div className="panel-heading">
                <div>
                    <span className="eyebrow">AI Feedback</span>
                    <h2>Learning Diagnosis</h2>
                </div>
                <div className={`status-pill ${status === 'Pass' ? 'pass' : 'retry'}`}>
                    {status || 'Awaiting answers'}
                </div>
            </div>

            <div className="feedback-grid">
                <div>
                    <span>Semantic score</span>
                    <strong>{semanticScore != null ? `${semanticScore}%` : '—'}</strong>
                </div>
                <div>
                    <span>Retries</span>
                    <strong>{retryCount ?? 0}</strong>
                </div>
            </div>

            <div className="weak-areas">
                <span>Weak areas</span>
                {weakAreas?.length ? (
                    <ul>
                        {weakAreas.map((area, index) => (
                            <li key={index}>{area}</li>
                        ))}
                    </ul>
                ) : (
                    <p className="hint-text">No weak concepts detected yet. Submit answers to assess.</p>
                )}
            </div>
        </section>
    );
}
