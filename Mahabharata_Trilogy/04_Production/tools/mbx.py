#!/usr/bin/env python3
"""mbx.py — Mahabharata Trilogy production compiler (stdlib only).

Single source of truth = the Markdown bibles in 04_Production/.
Commands (run from anywhere):
  python3 tools/mbx.py census     -> 01b_Cast_Census_GENERATED.md + build/cast_looks.csv
  python3 tools/mbx.py locations  -> build/locations.csv (validates 02_Location_Bible.md)
  python3 tools/mbx.py compile    -> parses Part*/P*C*.md shooting scripts and writes
                                     build/<chapter>_prompts.md, build/<chapter>_shots.csv,
                                     build/<chapter>_vo.csv, build/cue_sheet.csv,
                                     build/sfx_usage.csv, 05_Scene_Index_GENERATED.md
  python3 tools/mbx.py check      -> validation only (unknown IDs, missing DNA, timing)
  python3 tools/mbx.py all        -> census + locations + compile
"""
import csv, os, re, sys
from collections import OrderedDict, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 04_Production
BUILD = os.path.join(ROOT, 'build')
CAST_MD = os.path.join(ROOT, '01_Cast_and_Look_Bible.md')
LOC_MD = os.path.join(ROOT, '02_Location_Bible.md')
AUDIO_MD = os.path.join(ROOT, '03_Audio_Bible.md')
PARTS = ('P1', 'P2', 'P3')
PART_NAME = {'P1': 'भाग १ — प्रतिज्ञा और सभा', 'P2': 'भाग २ — वन और शंख',
             'P3': 'भाग ३ — कुरुक्षेत्र और स्वर्गारोहण'}
ID_RE = re.compile(r'^[A-Z][A-Z0-9]*_[A-Z0-9_]+$')


def cells(line):
    line = line.strip()
    if not line.startswith('|') or set(line) <= set('|-: '):
        return None
    parts = [c.strip() for c in line.strip('|').split('|')]
    return parts


def read_tables(path):
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path, encoding='utf-8') as f:
        for ln in f:
            c = cells(ln)
            if c:
                rows.append(c)
    return rows


def parts_of(s):
    return [p for p in PARTS if p in s]


# ---------------------------------------------------------------- cast
def load_cast():
    chars, looks, groups, extras, creatures = OrderedDict(), OrderedDict(), OrderedDict(), OrderedDict(), OrderedDict()
    for c in read_tables(CAST_MD):
        k = c[0]
        if k.startswith('CH_') and len(c) >= 7:
            chars[k] = dict(id=k, name=c[1], tier=c[2], face=c[3], never=c[4], ce=c[5], vox=c[6])
        elif len(c) >= 8 and c[1].startswith('CH_') and ID_RE.match(k):
            looks[k] = dict(id=k, char=c[1], name=c[2], age=c[3], parts=parts_of(c[4]),
                            sheet=c[5], used=c[6], dna=c[7])
        elif k.startswith('GRP_') and len(c) >= 4:
            groups[k] = dict(id=k, members=[m.strip() for m in c[1].split(',')], parts=parts_of(c[2]), comp=c[3])
        elif k.startswith('X_') and len(c) >= 4:
            extras[k] = dict(id=k, type=c[1], parts=parts_of(c[2]), dna=c[3])
        elif k.startswith('CR_') and len(c) >= 4:
            creatures[k] = dict(id=k, name=c[1], parts=parts_of(c[2]), dna=c[3])
    return chars, looks, groups, extras, creatures


def look_dna(look, chars):
    ch = chars.get(look['char'], {})
    face = ch.get('face', '')
    return f"{face}; {look['dna']}" if face else look['dna']


def sheet_unit(look):
    s = look['sheet']
    if s.startswith('group:'):
        return s.split(':', 1)[1]
    if s == 'vfx':
        return None
    return look['id']


STYLE_SHEET = ("photoreal character reference sheet, 65mm large-format film still look, Iron Age India c. 1000 BCE "
               "(hand-loom cotton, wild silk, deerskin, bark cloth, bronze and iron, gold worked by hand), "
               "real skin texture with pores, natural soft studio light, plain mid-grey seamless background")
SHEET_LAYOUT = ("layout: full-body front, three-quarter, profile and back views in one row; below them head close-ups "
                "with neutral, rage and grief expressions; identical face, body and costume in every view")
SHEET_NEG = "text, captions, watermark, logo, modern clothing, plastic jewellery, glowing aura, halo, fantasy armour"


def cmd_census():
    chars, looks, groups, extras, creatures = load_cast()
    os.makedirs(BUILD, exist_ok=True)
    errors = []
    for l in looks.values():
        if l['char'] not in chars:
            errors.append(f"LOOK {l['id']}: unknown CHAR {l['char']}")
        if not l['parts']:
            errors.append(f"LOOK {l['id']}: no PARTS")
        s = l['sheet']
        if s.startswith('group:') and s.split(':', 1)[1] not in groups:
            errors.append(f"LOOK {l['id']}: unknown group {s}")
    for g in groups.values():
        for m in g['members']:
            if m not in looks:
                errors.append(f"GROUP {g['id']}: unknown member {m}")
    used_chars = OrderedDict()
    for l in looks.values():
        used_chars.setdefault(l['char'], []).append(l['id'])

    def char_parts(cid):
        ps = set()
        for lid in used_chars.get(cid, []):
            ps.update(looks[lid]['parts'])
        return [p for p in PARTS if p in ps]

    stats = {}
    for p in PARTS + ('ALL',):
        sel = [l for l in looks.values() if p == 'ALL' or p in l['parts']]
        cset = OrderedDict((l['char'], 1) for l in sel)
        speaking = [c for c in cset if chars.get(c, {}).get('vox', '—') not in ('—', '')]
        tiers = defaultdict(int)
        for c in cset:
            tiers[chars[c]['tier']] += 1
        units = OrderedDict()
        vfx = 0
        for l in sel:
            u = sheet_unit(l)
            if u is None:
                vfx += 1
            else:
                units[u] = 1
        ex = [x for x in extras.values() if p == 'ALL' or p in x['parts']]
        cr = [x for x in creatures.values() if p == 'ALL' or p in x['parts']]
        stats[p] = dict(chars=len(cset), speaking=len(speaking), tiers=dict(tiers), looks=len(sel),
                        sheets=len(units), vfx=vfx, extras=len(ex), creatures=len(cr), char_ids=list(cset))

    # sheets first needed in each part (production order)
    first_need = OrderedDict((p, []) for p in PARTS)
    seen = set()
    for p in PARTS:
        for l in looks.values():
            if p in l['parts']:
                u = sheet_unit(l)
                if u and u not in seen:
                    seen.add(u)
                    first_need[p].append(u)

    out = []
    w = out.append
    w('# CAST CENSUS — AUTO-GENERATED (do not edit by hand)')
    w(f'Source: `01_Cast_and_Look_Bible.md` · generator: `tools/mbx.py census`\n')
    w('## 1. Kitne characters lagenge — summary\n')
    w('| | भाग १ | भाग २ | भाग ३ | **पूरी त्रयी (unique)** |')
    w('|---|---|---|---|---|')
    def row(label, key):
        w(f"| {label} | {stats['P1'][key]} | {stats['P2'][key]} | {stats['P3'][key]} | **{stats['ALL'][key]}** |")
    row('Named characters / beings (on screen)', 'chars')
    row('…of which speaking (own voice ID)', 'speaking')
    row('Looks (age + costume states)', 'looks')
    row('**Reference sheets to make** (group sheet = 1)', 'sheets')
    row('VFX design boards (no face sheet)', 'vfx')
    row('Extras crowd-type sheets', 'extras')
    row('Creature / animal / emblem sheets', 'creatures')
    for t in ('T1', 'T2', 'T3'):
        w(f"| Tier {t} characters | {stats['P1']['tiers'].get(t,0)} | {stats['P2']['tiers'].get(t,0)} | {stats['P3']['tiers'].get(t,0)} | **{stats['ALL']['tiers'].get(t,0)}** |")
    total_sheets = stats['ALL']['sheets'] + stats['ALL']['extras'] + stats['ALL']['creatures']
    w(f"\n**Grand total reference images (characters + extras + creatures): {total_sheets}** "
      f"(+ {stats['ALL']['vfx']} VFX design boards).\n")
    w('## 2. Production order — sheets that must exist BEFORE each part starts\n')
    w('| Part | New character sheets | Carried over from earlier parts |')
    w('|---|---|---|')
    carried = 0
    for p in PARTS:
        need_here = OrderedDict()
        for l in looks.values():
            if p in l['parts']:
                u = sheet_unit(l)
                if u:
                    need_here[u] = 1
        new = len(first_need[p])
        w(f"| {PART_NAME[p]} | **{new}** | {len(need_here) - new} |")
    w('\nTier key: **T1** hero (full turnaround + expressions, every look) · **T2** supporting (full sheet) · **T3** cameo (single sheet or group sheet).\n')

    w('## 3. Part-wise cast list (CHAR → looks used in that part)\n')
    for p in PARTS:
        w(f'### {PART_NAME[p]} — {stats[p]["chars"]} characters · {stats[p]["looks"]} looks · {stats[p]["sheets"]} sheets\n')
        w('| Tier | CHAR | नाम | Looks in this part | Voice |')
        w('|---|---|---|---|---|')
        for cid in sorted(stats[p]['char_ids'], key=lambda c: (chars[c]['tier'], list(chars).index(c))):
            ls = [lid for lid in used_chars[cid] if p in looks[lid]['parts']]
            w(f"| {chars[cid]['tier']} | `{cid}` | {chars[cid]['name']} | {' · '.join('`'+x+'`' for x in ls)} | {chars[cid]['vox']} |")
        w('')
    w('## 4. Group sheets\n')
    for g in groups.values():
        w(f"* `{g['id']}` ({', '.join(g['parts'])}): {', '.join(g['members'])} — {g['comp']}")
    w('\n## 5. Sheet-generation prompts (copy-paste; one per sheet)\n')
    w('Use the same image model for every sheet; for every later look of a character, attach that character\'s FIRST approved sheet as the face reference.\n')
    for cid, lids in used_chars.items():
        ch = chars[cid]
        w(f"<details><summary><b>{cid}</b> — {ch['name']} ({ch['tier']}, {len(lids)} looks)</summary>\n")
        for lid in lids:
            l = looks[lid]
            if l['sheet'] == 'vfx':
                w(f"**{lid} · {l['name']}** — VFX design board (no face sheet): {l['dna']}\n")
                continue
            if l['sheet'].startswith('group:'):
                w(f"**{lid} · {l['name']}** — part of group sheet `{l['sheet'][6:]}`\n")
                continue
            w(f"**{lid} · {l['name']} · age {l['age']} · {', '.join(l['parts'])}**")
            w('```text')
            w(f"{STYLE_SHEET}. Subject: {look_dna(l, chars)}. {SHEET_LAYOUT}.")
            w(f"Avoid: {SHEET_NEG}{'; ' + ch['never'] if ch['never'] not in ('—', '') else ''}.")
            w('```')
        w('</details>\n')
    for gid, g in groups.items():
        w(f"<details><summary><b>{gid}</b> — group sheet</summary>\n")
        w('```text')
        mem = '; '.join(f"{m}: {look_dna(looks[m], chars)}" for m in g['members'] if m in looks)
        w(f"{STYLE_SHEET}. Group reference sheet — {g['comp']}. Characters: {mem}. Each figure full-body front and 3/4, face close-up; same lighting.")
        w(f"Avoid: {SHEET_NEG}.")
        w('```\n</details>\n')
    w('## 6. Extras & creatures (one sheet each)\n')
    for x in extras.values():
        w(f"* `{x['id']}` ({', '.join(x['parts'])}) — {x['type']}: `{STYLE_SHEET}. Crowd type sheet: {x['dna']}; six varied individuals, full body.`")
    for x in creatures.values():
        w(f"* `{x['id']}` ({', '.join(x['parts'])}) — {x['name']}: `photoreal wildlife reference, natural light: {x['dna']}; side, front and 3/4 views.`")
    if errors:
        w('\n## ⚠ VALIDATION ERRORS\n')
        for e in errors:
            w(f'* {e}')
    with open(os.path.join(ROOT, '01b_Cast_Census_GENERATED.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    with open(os.path.join(BUILD, 'cast_looks.csv'), 'w', encoding='utf-8', newline='') as f:
        cw = csv.writer(f)
        cw.writerow(['LOOK', 'CHAR', 'NAME', 'LOOK_NAME', 'AGE', 'PARTS', 'SHEET', 'USED_IN', 'VOX', 'FULL_DNA', 'NEVER'])
        for l in looks.values():
            ch = chars.get(l['char'], {})
            cw.writerow([l['id'], l['char'], ch.get('name', ''), l['name'], l['age'], ' '.join(l['parts']),
                         l['sheet'], l['used'], ch.get('vox', ''), look_dna(l, chars), ch.get('never', '')])
    print('census:', {p: {k: v for k, v in stats[p].items() if k != 'char_ids'} for p in stats})
    if errors:
        print('ERRORS:', *errors, sep='\n  ')
    return stats, errors


# ---------------------------------------------------------------- locations
def load_locations():
    locs = OrderedDict()
    for c in read_tables(LOC_MD):
        if c[0].startswith('LOC_') and len(c) >= 5:
            locs[c[0]] = dict(id=c[0], name=c[1], parts=parts_of(c[2]), dna=c[3], light=c[4])
    return locs


def load_style():
    style = OrderedDict()
    for c in read_tables(LOC_MD):
        if c[0].startswith('STY_') and len(c) >= 2:
            style[c[0]] = c[1]
    return style


def cmd_locations():
    locs = load_locations()
    os.makedirs(BUILD, exist_ok=True)
    with open(os.path.join(BUILD, 'locations.csv'), 'w', encoding='utf-8', newline='') as f:
        cw = csv.writer(f)
        cw.writerow(['LOC', 'NAME', 'PARTS', 'DNA', 'LIGHT_VARIANTS'])
        for l in locs.values():
            cw.writerow([l['id'], l['name'], ' '.join(l['parts']), l['dna'], l['light']])
    print('locations:', len(locs), {p: sum(1 for l in locs.values() if p in l['parts']) for p in PARTS})
    return locs


# ---------------------------------------------------------------- audio
def mmss(x):
    m = re.match(r'^(\d+):(\d\d)$', (x or '').strip())
    return int(m.group(1)) * 60 + int(m.group(2)) if m else 0


def audio_totals(cues, sfx, vox):
    t = defaultdict(lambda: [0, 0])
    for c in cues.values():
        key = ('THEME-' if c['id'].startswith('THM_') else '') + c['tool']
        t[key][0] += 1
        t[key][1] += mmss(c['dur'])
    loops = sum(1 for x in sfx.values() if 'LOOP' in x.get('len', ''))
    return t, len(sfx), loops, len(vox)


def load_audio():
    cues, sfx, vox = OrderedDict(), OrderedDict(), OrderedDict()
    for c in read_tables(AUDIO_MD):
        k = c[0]
        if k.startswith('SFX_') and len(c) >= 4:
            sfx[k] = dict(id=k, name=c[1], tool=c[2], prompt=c[3], len=(c[4] if len(c) > 4 else ''))
        elif re.match(r'^VOX_', k) and len(c) >= 4:
            vox[k] = dict(id=k, who=c[1], design=c[2], settings=c[3])
        elif re.match(r'^(MUS|THM)_', k) and len(c) >= 4:
            cues[k] = dict(id=k, name=c[1], tool=c[2], prompt=c[3], dur=(c[4] if len(c) > 4 else ''))
    return cues, sfx, vox


# ---------------------------------------------------------------- shooting scripts
SCENE_RE = re.compile(r'^##\s+(P[123]C\d\dS\d\d)\s*·\s*(.+?)\s*·\s*⏱\s*(\d+):(\d\d)\s*$')
CH_RE = re.compile(r'^#\s+(P[123]C\d\d)\s*·\s*(.+)$')
LINE_RE = re.compile(r'^-\s*(L\d{2,3})\s*·\s*([A-Z0-9_]+|VO|SFX)\s*(?:\(([^)]*)\))?\s*·\s*(VOX_[A-Z0-9_]+|—)\s*·\s*(\[[^\]]*\])?\s*(.*)$')
META_RE = re.compile(r'^-\s*\*\*(LOC|CAST|CE|HOOK|MUSIC|AMB|SFX|NOTE|BEAT)\*\*\s*:\s*(.*)$')
SHOT_HDR = ['SHOT', 'SEC', 'MODE', 'CAST', 'CAMERA', 'ACTION', 'LINES', 'SOUND']


def parse_chapter(path):
    ch = dict(id=None, title='', scenes=[], path=path)
    sc = None
    with open(path, encoding='utf-8') as f:
        for raw in f:
            ln = raw.rstrip('\n')
            m = CH_RE.match(ln)
            if m and not ch['id']:
                ch['id'], ch['title'] = m.group(1), m.group(2).strip()
                continue
            m = SCENE_RE.match(ln)
            if m:
                sc = dict(id=m.group(1), head=m.group(2), dur=int(m.group(3)) * 60 + int(m.group(4)),
                          meta=defaultdict(str), shots=[], lines=OrderedDict())
                ch['scenes'].append(sc)
                continue
            if sc is None:
                continue
            m = META_RE.match(ln)
            if m:
                sc['meta'][m.group(1)] += (' ' if sc['meta'][m.group(1)] else '') + m.group(2).strip()
                continue
            m = LINE_RE.match(ln)
            if m:
                sc['lines'][m.group(1)] = dict(id=m.group(1), who=m.group(2), mod=m.group(3) or '',
                                               vox=m.group(4), tag=(m.group(5) or ''), text=m.group(6).strip())
                continue
            c = cells(ln)
            if c and len(c) >= 8 and re.match(r'^\d{2}[a-z]?$', c[0]):
                sc['shots'].append(dict(zip(SHOT_HDR, c[:8])))
    return ch


def expand_secs(sec):
    m = re.match(r'^(\d+)\s*[x×]\s*(\d+)$', sec.strip())
    if m:
        return int(m.group(1)), int(m.group(2))
    m = re.match(r'^(\d+)$', sec.strip())
    if m:
        return int(m.group(1)), 1
    return 8, 1


def line_ids(spec, scene_lines):
    spec = spec.strip()
    if not spec or spec == '—':
        return []
    ids = []
    for part in re.split(r'[,\s]+', spec):
        m = re.match(r'^L(\d{2,3})[–-]L?(\d{2,3})$', part)
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            width = len(m.group(1))
            ids += [f'L{n:0{width}d}' for n in range(a, b + 1)]
        elif re.match(r'^L\d{2,3}$', part):
            ids.append(part)
    return ids


def cmd_compile(check_only=False):
    chars, looks, groups, extras, creatures = load_cast()
    locs = load_locations()
    style = load_style()
    cues, sfx, vox = load_audio()
    os.makedirs(BUILD, exist_ok=True)
    chapters = []
    for part_dir in ('Part1', 'Part2', 'Part3'):
        d = os.path.join(ROOT, part_dir)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if re.match(r'^P[123]C\d\d.*\.md$', fn):
                chapters.append(parse_chapter(os.path.join(d, fn)))
    problems = []
    index = []
    cue_rows, sfx_use, vo_all = [], defaultdict(list), []
    look_use = defaultdict(set)
    style_master = style.get('STY_MASTER', '')
    neg_master = style.get('STY_NEGATIVE', '')
    for ch in chapters:
        if not ch['id']:
            problems.append(f"{ch['path']}: missing '# P#C## · title' header")
            continue
        prompts_md, shots_csv, vo_csv = [], [], []
        prompts_md.append(f"# {ch['id']} · {ch['title']} — COMPILED CLIP PROMPTS (auto-generated)\n")
        prompts_md.append("Paste each block into Google Flow. Attach the listed reference sheets as Ingredients. "
                          "Line text is for lip-shape only; final voice = ElevenLabs (see _vo.csv).\n")
        t_ch = 0
        for sc in ch['scenes']:
            t_ch += sc['dur']
            loc_ids = re.findall(r'LOC_[A-Z0-9_]+', sc['meta']['LOC'])
            for lid in loc_ids:
                if lid not in locs:
                    problems.append(f"{sc['id']}: unknown location {lid}")
            cast_ids = re.findall(r'\b[A-Z][A-Z0-9]*_[A-Z0-9]+\b', sc['meta']['CAST'])
            for cid in cast_ids:
                if cid not in looks and cid not in extras and cid not in creatures:
                    problems.append(f"{sc['id']}: unknown cast id {cid}")
                else:
                    look_use[cid].add(ch['id'][:2])
            for k in ('MUSIC',):
                for cue in re.findall(r'\b(?:MUS|THM)_[A-Z0-9_]+\b', sc['meta'][k]):
                    if cue not in cues:
                        problems.append(f"{sc['id']}: unknown music cue {cue}")
                    cue_rows.append([ch['id'], sc['id'], cue, cues.get(cue, {}).get('tool', '?'), sc['meta'][k]])
            for s_id in re.findall(r'\bSFX_[A-Z0-9_]+\b', sc['meta']['SFX'] + ' ' + sc['meta']['AMB']):
                sfx_use[s_id].append(sc['id'])
            index.append([ch['id'], sc['id'], sc['head'], sc['dur'], ' '.join(loc_ids), ' '.join(cast_ids),
                          sc['meta']['CE'], sc['meta']['HOOK']])
            shot_secs = 0
            loc_dna = ' '.join(f"{locs[l]['dna']}" for l in loc_ids if l in locs)
            prompts_md.append(f"\n## {sc['id']} · {sc['head']} · {sc['dur']//60}:{sc['dur']%60:02d}\n")
            for sh in sc['shots']:
                secs, n = expand_secs(sh['SEC'])
                shot_secs += secs * n
                sh_cast = re.findall(r'\b[A-Z][A-Z0-9]*_[A-Z0-9]+\b', sh['CAST'])
                dna_parts, refs = [], []
                for cid in sh_cast:
                    if cid in looks:
                        lk = looks[cid]
                        dna_parts.append(f"[{cid}] {look_dna(lk, chars)}")
                        refs.append(cid if not lk['sheet'].startswith('group:') else lk['sheet'][6:])
                        look_use[cid].add(ch['id'][:2])
                    elif cid in extras:
                        dna_parts.append(f"[{cid}] {extras[cid]['dna']}")
                        refs.append(cid)
                    elif cid in creatures:
                        dna_parts.append(f"[{cid}] {creatures[cid]['dna']}")
                        refs.append(cid)
                    else:
                        problems.append(f"{sc['id']}-{sh['SHOT']}: unknown cast id {cid}")
                lids = line_ids(sh['LINES'], sc['lines'])
                for lid in lids:
                    if lid not in sc['lines']:
                        problems.append(f"{sc['id']}-{sh['SHOT']}: line {lid} not defined in scene")
                for s_id in re.findall(r'\bSFX_[A-Z0-9_]+\b', sh['SOUND']):
                    sfx_use[s_id].append(f"{sc['id']}-{sh['SHOT']}")
                takes = max(n, len(lids)) if lids else n
                for k in range(takes):
                    lid = lids[k] if k < len(lids) else None
                    ln = sc['lines'].get(lid) if lid else None
                    clip_id = f"{sc['id']}-{sh['SHOT']}" + (f".{k+1}" if takes > 1 else '')
                    speak = ''
                    if ln and ln['who'] not in ('VO', 'SFX') and ln['mod'].strip().upper() not in ('V.O.', 'VO', 'O.S.'):
                        speak = f" The character [{ln['who']}] speaks in Hindi, lips clearly visible: \"{ln['text']}\""
                    cam = re.sub(r'\bSTY_[A-Z]+\b', lambda m: style.get(m.group(0), m.group(0)), sh['CAMERA'])
                    act = re.sub(r'\bSTY_[A-Z]+\b', lambda m: style.get(m.group(0), m.group(0)), sh['ACTION'])
                    prompt = (f"{style_master} LOCATION: {loc_dna} CAST: {' | '.join(dna_parts) if dna_parts else 'no characters'}. "
                              f"SHOT: {cam}. ACTION: {act}.{speak} AUDIO: {sh['SOUND']}.").strip()
                    prompts_md.append(f"**{clip_id}** · {secs}s · mode `{sh['MODE']}` · refs: {', '.join(refs) or '—'}"
                                      + (f" · line {lid}" if lid else ''))
                    prompts_md.append('```text\n' + prompt + f"\nAVOID: {neg_master}\n```")
                    shots_csv.append([clip_id, secs, sh['MODE'], ' '.join(refs), ' '.join(loc_ids), sh['CAMERA'],
                                      sh['ACTION'], lid or '', sh['SOUND'], prompt])
            if sc['shots'] and abs(shot_secs - sc['dur']) > max(20, sc['dur'] * 0.35):
                problems.append(f"{sc['id']}: shot seconds {shot_secs} vs scene duration {sc['dur']} (edit will trim; check coverage)")
            for ln in sc['lines'].values():
                if ln['vox'] != '—' and ln['vox'] not in vox:
                    problems.append(f"{sc['id']} {ln['id']}: unknown voice {ln['vox']}")
                vo_csv.append([sc['id'], ln['id'], ln['who'], ln['mod'], ln['vox'], ln['tag'], ln['text']])
                vo_all.append([ch['id'], sc['id'], ln['id'], ln['who'], ln['vox'], ln['tag'], ln['text']])
        if not check_only:
            with open(os.path.join(BUILD, f"{ch['id']}_prompts.md"), 'w', encoding='utf-8') as f:
                f.write('\n'.join(prompts_md) + '\n')
            with open(os.path.join(BUILD, f"{ch['id']}_shots.csv"), 'w', encoding='utf-8', newline='') as f:
                cw = csv.writer(f); cw.writerow(['CLIP', 'SEC', 'MODE', 'REFS', 'LOC', 'CAMERA', 'ACTION', 'LINE', 'SOUND', 'PROMPT'])
                cw.writerows(shots_csv)
            with open(os.path.join(BUILD, f"{ch['id']}_vo.csv"), 'w', encoding='utf-8', newline='') as f:
                cw = csv.writer(f); cw.writerow(['SCENE', 'LINE', 'WHO', 'MOD', 'VOX', 'TAGS', 'TEXT'])
                cw.writerows(vo_csv)
        ch['runtime'] = t_ch
        ch['clips'] = len(shots_csv)
        ch['vo_chars'] = sum(len(r[6]) for r in vo_csv)
    if not check_only:
        with open(os.path.join(BUILD, 'cue_sheet.csv'), 'w', encoding='utf-8', newline='') as f:
            cw = csv.writer(f); cw.writerow(['CHAPTER', 'SCENE', 'CUE', 'TOOL', 'NOTE']); cw.writerows(cue_rows)
        with open(os.path.join(BUILD, 'sfx_usage.csv'), 'w', encoding='utf-8', newline='') as f:
            cw = csv.writer(f); cw.writerow(['SFX', 'DEFINED', 'USES', 'WHERE'])
            for k in sorted(sfx_use):
                cw.writerow([k, 'yes' if k in sfx else 'NO', len(sfx_use[k]), ' '.join(sfx_use[k][:40])])
        with open(os.path.join(BUILD, 'vo_all.csv'), 'w', encoding='utf-8', newline='') as f:
            cw = csv.writer(f); cw.writerow(['CHAPTER', 'SCENE', 'LINE', 'WHO', 'VOX', 'TAGS', 'TEXT']); cw.writerows(vo_all)
        # scene index
        out = ['# SCENE INDEX — AUTO-GENERATED from the shooting scripts (`tools/mbx.py compile`)\n']
        tot = defaultdict(int)
        for ch in chapters:
            if ch['id']:
                tot[ch['id'][:2]] += ch.get('runtime', 0)
        out.append('| Part | Chapters | Runtime | Clips (8s/4s/6s gens) | VO characters (ElevenLabs) |')
        out.append('|---|---|---|---|---|')
        for p in PARTS:
            chs = [c for c in chapters if c['id'] and c['id'].startswith(p)]
            if chs:
                out.append(f"| {PART_NAME[p]} | {len(chs)} | {tot[p]//60} min {tot[p]%60:02d} s | "
                           f"{sum(c['clips'] for c in chs)} | {sum(c['vo_chars'] for c in chs):,} |")
        for ch in chapters:
            if not ch['id']:
                continue
            out.append(f"\n## {ch['id']} · {ch['title']} — {ch['runtime']//60}:{ch['runtime']%60:02d} · {ch['clips']} clips\n")
            out.append('| Scene | Heading | Dur | LOC | Cast | CE | Hook |')
            out.append('|---|---|---|---|---|---|---|')
            for r in index:
                if r[0] == ch['id']:
                    out.append(f"| {r[1]} | {r[2]} | {r[3]//60}:{r[3]%60:02d} | {r[4]} | {r[5]} | {r[6]} | {r[7]} |")
        t, nsfx, nloop, nvox = audio_totals(cues, sfx, vox)
        out.append('\n## Audio totals (from 03_Audio_Bible.md + scripts)\n')
        out.append('| Item | Count | Minutes |')
        out.append('|---|---|---|')
        for key in sorted(t):
            out.append(f"| {key} | {t[key][0]} | {t[key][1]//60}:{t[key][1]%60:02d} |")
        out.append(f"| ElevenLabs SFX defined (of which seamless loops) | {nsfx} ({nloop}) | — |")
        out.append(f"| Voices defined (VOX) | {nvox} | — |")
        vo_chars = sum(len(r[6]) for r in vo_all)
        out.append(f"| Dialogue + narration lines | {len(vo_all)} | {vo_chars:,} characters for TTS/STS |")
        undefined = sorted(k for k in sfx_use if k not in sfx)
        if undefined:
            problems += [f"SFX used but not defined in 03_Audio_Bible.md: {k}" for k in undefined]
        if problems:
            out.append('\n## ⚠ VALIDATION\n')
            out += [f'* {p}' for p in problems]
        with open(os.path.join(ROOT, '05_Scene_Index_GENERATED.md'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(out) + '\n')
    print('chapters:', len(chapters), 'scenes:', len(index), 'problems:', len(problems))
    for p in problems[:60]:
        print('  -', p)
    return problems


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if cmd == 'census':
        cmd_census()
    elif cmd == 'locations':
        cmd_locations()
    elif cmd == 'compile':
        cmd_compile()
    elif cmd == 'check':
        cmd_compile(check_only=True)
    elif cmd == 'all':
        cmd_census(); cmd_locations(); cmd_compile()
    else:
        print(__doc__)
