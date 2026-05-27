export default function LogsCard({ messages }) {
    return (
        <section className="panel-card logs-card glass-card">
            <div className="panel-heading">
                <span className="eyebrow">Session Logs</span>
                <h2>Activity Timeline</h2>
            </div>
            <ul className="logs-list">
                {messages?.length ? (
                    messages.map((message, index) => (
                        <li key={`${message}-${index}`} className="log-entry">
                            <span className="log-bullet" />
                            {message}
                        </li>
                    ))
                ) : (
                    <li className="log-empty">No session activity yet. Start a learning session to see logs.</li>
                )}
            </ul>
        </section>
    );
}
