"""Run the AI decision helper: python main.py [--out-dir output]"""

import argparse

from ai_triage.report import write_all


def main():
    parser = argparse.ArgumentParser(description="Decide whether each requirement really needs AI.")
    parser.add_argument("--out-dir", default="output", help="folder for report.csv, report.md, lifecycle.md")
    args = parser.parse_args()

    rows = write_all(args.out_dir)

    print(f"{'#':>2}  {'Requirement':<52} Decision")
    print("-" * 85)
    for r in rows:
        print(f"{r['id']:>2}  {r['requirement']:<52} {r['decision']}")
    ai = sum(r["decision"] in ("Classical ML", "Deep Learning", "Generative AI") for r in rows)
    print(f"\n{ai} of {len(rows)} requirements need AI; {len(rows) - ai} do not.")
    print(f"Reports written to: {args.out_dir}/ (report.csv, report.md, lifecycle.md)")


if __name__ == "__main__":
    main()
