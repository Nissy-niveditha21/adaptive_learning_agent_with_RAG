export default function Navbar() {
    return (
        <header className="navbar shell-card">
            <div>
                <p className="brand-tag">AI Learning Agent</p>
                <span className="brand-subtitle">Checkpoint-based AI tutoring</span>
            </div>

            <div className="status-pill">
                <span className="status-dot connected" />
                Backend Connected
            </div>
        </header>
    );
}
