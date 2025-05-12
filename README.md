1. LangFuse one of the best UI, open-source
2. Get overview of all the interarctions with LLMs (many mondels not only openai)
What Other Functionalities you can use with Trace?
Langfuse traces are very powerful.
Here are some important things you can do:


Feature	How it helps
Metadata	Attach extra information (e.g., model name, temperature, cost, prompt tokens, response tokens).
Scores	Log evaluation metrics (e.g., "this response got ROUGE-1 score 0.45").
Events	Add custom events during the trace (e.g., "retry started", "validation failed").
Observability Spans	Break down steps into small spans inside the same trace (e.g., "prompt building", "calling LLM", "post-processing").
Retries	Show automatic retries inside the same trace so you can analyze them later.
Error Tracking	Mark spans or traces as errored if something fails (you can later filter all error traces in dashboard).
Hierarchical view	See parent/child relations between spans (helpful if you chain calls).
