export default function ProgressCard({ topic, checkpoint, completed, total, score, progress }) {
    return (
        <section className="panel-card progress-card glass-card">
            <div className="panel-heading">
                <div>
                    <span className="eyebrow">Checkpoint Progress</span>
                    <h2>{topic || 'Active Topic'}</h2>
                    <p className="checkpoint-title">{checkpoint || 'Loading current checkpoint…'}</p>
                </div>
                <div className="score-badge">{score ? `${score}%` : '—'}</div>
            </div>

            <div className="progress-meta">
                <div>
                    <span>Completed checkpoints</span>
                    <strong>{completed}/{total}</strong>
                </div>
                <div>
                    <span>Progress</span>
                    <strong>{progress}%</strong>
                </div>
            </div>

            <div className="progress-bar" aria-hidden="true">
                <div className="progress-fill" style={{ width: `${progress}%` }} />
            </div>
        </section>
    );
}
