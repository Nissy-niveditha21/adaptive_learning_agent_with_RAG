export default function QuestionCard({ index, question, answer, onChange }) {
    return (
        <article className="panel-card question-card glass-card">
            <div className="question-header">
                <span className="question-index">Question {index + 1}</span>
                <p>{question}</p>
            </div>
            <textarea
                value={answer}
                onChange={(event) => onChange(event.target.value)}
                placeholder="Write your answer here..."
                className="answer-input"
                rows={4}
            />
        </article>
    );
}
