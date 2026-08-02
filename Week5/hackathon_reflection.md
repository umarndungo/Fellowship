# Hackathon #1 Reflection: KPC Maintenance Dispatch Engine

Participating in Hackathon #1 to build an automated maintenance dispatch pipeline for KPC was an intense, high-value learning experience. 

Our task required ingesting unstructured field work orders, running a strict 9-point quality gate, and auto-dispatching high-priority tickets in under 0.2 seconds.

## Challenges

### Version Control

Our biggest technical hurdle centered on version control and codebase integration. As team members worked on different components of the ingestion pipeline and CMMS API scheduler, overlapping changes led to severe Git merge conflicts and branch sync issues, which temporarily stalled our pipeline deployment. 

We resolved this by establishing clear file ownership, setting up a shared integration branch, and running regular step-by-step pair debugging sessions to resolve conflicts together without losing critical code logic.

### Solution Development

Additionally, aligning on a single architectural vision proved challenging early on, as differing solution approaches created friction and delayed feature polished execution.

## Looking Forward

Looking ahead to the next hackathon, I will approach teamwork with three distinct improvements:
1. **Upfront Problem Decomposition:** Spend more time dissecting the system architecture and agreeing on unified data flows before writing any code.
2. **Mastering Collaborative Git:** Adopt a cleaner branching strategy with standard pull request reviews.
3. **Proactive Communication:** Personally improve my active communication habits to keep the team aligned in real time.