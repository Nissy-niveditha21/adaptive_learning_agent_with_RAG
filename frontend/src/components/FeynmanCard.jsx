import ReactMarkdown from 'react-markdown';

export default function FeynmanCard({ explanation }) {
    return (
        <section className="panel-card feynman-card glass-card">
            <div className="panel-heading">
                <span className="eyebrow">Feynman Explanation</span>
                <h2>Deep Concept Clarity</h2>
            </div>
            <div className="markdown-body">
                <ReactMarkdown>{explanation || 'The AI tutor will generate an explanation once a learning session begins.'}</ReactMarkdown>
            </div>
        </section>
    );
}
