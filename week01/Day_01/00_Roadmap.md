# SWE / SDE Interview-Ready Roadmap (Python Track)

**Start:** Mon Oct 19, 2026 · **Finish:** Fri Dec 4, 2026 · **7 weeks of weekdays (35 days), 6–8 hrs/day**

> **Why 7 weeks and not 4?** Going from beginner to interview-ready for SDE I / New Grad / Backend roles means covering Python, DSA (~150 LeetCode problems), backend/APIs, databases, DevOps basics, system design, and interview practice. Four weeks would mean skipping DSA reps, and DSA reps are what decide most coding rounds. Seven weeks is aggressive but realistic. If you move faster, we compress; if a skill needs more time, we adjust.
>
> **SDE II / L4 note:** These roles expect 2–4 years of experience. This plan gives you the *knowledge* for L4-style questions (system design, trade-offs). Real L4 readiness also comes from the projects in Week 6, which you'll talk about in interviews.

---

## How Each Day Works

Every full day has **two tracks**, the same way real interview prep works:

| Block | Time | What |
|---|---|---|
| **A. DSA + LeetCode** | ~3 hrs (morning) | One pattern per day: learn it, then solve 4–6 problems |
| **B. Engineering track** | ~3–4 hrs (afternoon) | Python → Backend → DBs → DevOps → System Design |
| **C. Review** | ~15 min | Daily check questions, then submit |

**Our loop:**
1. I give you `DayXX_Lesson.md` (lesson, exercises, LeetCode list, daily check).
2. You do the work and paste your **code + answers** here.
3. I return `DayXX_Review.md` with mistakes, hints, fixes, full solutions and explanations.
4. At the end of each **skill**, you get a **Skill Questionnaire (SQ)**. Based on your score we either move on or spend extra time.

**Tools you'll use:** Python 3.13+, VS Code, Git + GitHub, a free LeetCode account, PostgreSQL, Docker, Postman (or curl), and later Redis and an AWS free tier account.

---

## Week 1 — Foundations (Oct 19–23)

| Day | A. DSA / LeetCode | B. Engineering | Checkpoint |
|---|---|---|---|
| **D1 Mon** (2 hrs) | 2 warm-up problems | Setup + Python basics: types, strings, conditionals, loops | Daily check |
| **D2 Tue** | Big-O notation, time/space complexity | Python: lists, tuples, dicts, sets, comprehensions; functions, `*args/**kwargs`, scope | |
| **D3 Wed** | **Arrays & Hashing** (Two Sum, Contains Duplicate, Valid Anagram, Group Anagrams, Top K Frequent) | Python: OOP (classes, inheritance, dunder methods, `@property`, dataclasses) | |
| **D4 Thu** | **Strings** + prefix sums | Python: errors/exceptions, file I/O, modules, venv/pip, `collections`, `itertools`, generators, decorators, context managers | **SQ1: Python** |
| **D5 Fri** | Mixed review set (8 problems) | Git & GitHub (branching, PRs, merge conflicts), Linux/CLI essentials, pytest intro | **SQ2: Git/Linux/Testing** |

## Week 2 — Core Patterns + Web Fundamentals (Oct 26–30)

| Day | A. DSA / LeetCode | B. Engineering | Checkpoint |
|---|---|---|---|
| **D6** | **Two Pointers** | How the web works: TCP/IP, DNS, HTTP/HTTPS, status codes, headers, cookies | |
| **D7** | **Sliding Window** | REST API design: resources, verbs, idempotency, pagination, versioning, error formats | |
| **D8** | **Stack** (Valid Parentheses, Min Stack, Daily Temperatures…) | **FastAPI**: routes, Pydantic models, validation, dependency injection; build a Todo API | |
| **D9** | **Binary Search** (incl. search on answer) | SQL fundamentals: SELECT, JOINs, GROUP BY, subqueries, window functions (+ LeetCode SQL 50 set) | |
| **D10** | **Linked Lists** | PostgreSQL: schema design, normalization, indexes, transactions, ACID, isolation levels | **SQ3: DSA I** · **SQ4: HTTP/REST/SQL** |

## Week 3 — Trees + Production Backend (Nov 2–6)

| Day | A. DSA / LeetCode | B. Engineering | Checkpoint |
|---|---|---|---|
| **D11** | Recursion fundamentals | SQLAlchemy ORM + Alembic migrations; connect Todo API to Postgres | |
| **D12** | **Binary Trees** (DFS/BFS traversals) | Auth: hashing passwords, sessions vs JWT, OAuth2 flow, RBAC | |
| **D13** | **BST** + tree construction | Testing APIs: unit vs integration, fixtures, mocking, coverage, TDD | |
| **D14** | **Heaps / Priority Queue** | Docker: images, containers, Dockerfile, docker-compose (API + DB) | |
| **D15** | **Backtracking** (Subsets, Permutations, Combination Sum, N-Queens) | Build day: complete, tested, Dockerized API pushed to GitHub | **SQ5: DSA II** · **SQ6: Backend** |

## Week 4 — Graphs + Scaling Backend (Nov 9–13)

| Day | A. DSA / LeetCode | B. Engineering | Checkpoint |
|---|---|---|---|
| **D16** | **Graphs: BFS/DFS** (Number of Islands, Clone Graph…) | Caching: Redis, cache-aside, TTL, invalidation, cache stampede | |
| **D17** | **Topological Sort**, cycle detection | Async Python (`asyncio`), concurrency vs parallelism, threads, processes, the GIL | |
| **D18** | **Union-Find**, **Dijkstra** | Message queues: Celery, RabbitMQ, Kafka concepts; background jobs | |
| **D19** | **Intervals** + **Greedy** | CI/CD with GitHub Actions; logging, metrics, tracing (observability) | |
| **D20** | Mixed graph set (timed) | AWS essentials: EC2, S3, RDS, Lambda, IAM, VPC basics; deploy your API | **SQ7: Graphs** · **SQ8: Scaling/DevOps** |

## Week 5 — DP + System Design + QA (Nov 16–20)

| Day | A. DSA / LeetCode | B. Engineering | Checkpoint |
|---|---|---|---|
| **D21** | **1-D DP** (Climbing Stairs, House Robber, Coin Change…) | System design fundamentals: scaling, load balancers, CAP, consistency, replication, sharding | |
| **D22** | **2-D DP** (LCS, Edit Distance, Unique Paths) | Classic designs: URL shortener, rate limiter, key-value store | |
| **D23** | **Tries** + **Bit Manipulation** | Classic designs: news feed, chat app (WebSockets), notification system | |
| **D24** | Mixed hard set | Low-level design (OOD): parking lot, LRU cache, elevator; SOLID, design patterns | |
| **D25** | Timed mock (2 problems / 45 min) | QA/Automation: test pyramid, Playwright/Selenium, API test automation, load testing (Locust) | **SQ9: DSA III** · **SQ10: System Design** |

## Week 6 — Industry Projects (Nov 23–27) · *Thanksgiving Thu Nov 26: shift if needed*

Daily: 2 LeetCode problems (keep sharp) + 5 hrs building.

| Project | What you build | Skills proved |
|---|---|---|
| **P1: Production URL Shortener** | FastAPI + Postgres + Redis cache + rate limiting + Docker + CI + deployed to AWS | APIs, DB, caching, DevOps |
| **P2: E-commerce Order Service** | Orders, inventory, payments (mock), idempotency keys, background jobs via queue, full test suite | Transactions, consistency, async work, testing |
| **P3: Fix-the-broken-service** | I give you a buggy, slow codebase: find bugs, fix N+1 queries, add tests, add logging | Debugging, reading code (very common in real jobs and some interviews) |

## Week 7 — Interview Prep (Nov 30–Dec 4)

| Day | Focus |
|---|---|
| **D31** | Resume + GitHub polish; project storytelling; how to talk about trade-offs |
| **D32** | Behavioral: STAR method, Amazon Leadership Principles, "Googleyness", conflict/failure stories |
| **D33** | Mock coding interviews (I play interviewer: live coding, follow-ups, complexity) |
| **D34** | Mock system design + LLD interviews |
| **D35** | Company-specific prep (FAANG vs startup vs consulting/finance vs hardware like Micron/Nvidia/NetApp) + final readiness assessment |

---

## LeetCode Targets

- **~150 problems total** (NeetCode 150 style coverage) + **SQL 50**.
- Split: ~45% Easy, ~45% Medium, ~10% Hard.
- **Rule:** stuck 20 min on Easy / 35 min on Medium → read a hint → still stuck → read solution, then **re-solve from scratch next day**.
- Always say aloud: approach → complexity → code → test edge cases. That is exactly what interviewers grade.

## Progress Log

| Day | Date | Done? | Review score | Notes |
|---|---|---|---|---|
| D1 | Oct 19 | ☐ | | |
| D2 | Oct 20 | ☐ | | |
| D3 | Oct 21 | ☐ | | |
| D4 | Oct 22 | ☐ | | |
| D5 | Oct 23 | ☐ | | |
