#!/usr/bin/env python3

from sys import argv


def main():
    # get info from alignment VCF
    pos_info = {}
    with open(argv[2], "r") as alt_vcf_fi:
        for line in alt_vcf_fi.readlines():
            line = line.strip().split("\t")
            pos = line[0]
            ref = line[1]
            alt = line[2].split(",")
            if "N" in alt:
                if len(alt) > 1:
                    alt.remove("N")
                else:
                    alt[0] = "."
            alt = ",".join(alt)
            pos_info[int(pos)] = (ref, alt)

    # declare genome end positions
    genome_ends = [i+1 for i in range(55)] + [i+1 for i in range(29803, 29903)]

    with open(argv[1], "r") as vcf_fi:
        vcf_contents = [i.strip() for i in vcf_fi.readlines()]


    # process lines, adding ALT info and merging seq_end as appropriate
    vcf_lines = []
    seen_ends = []
    genome_end_line_dic = {}
    for vcf_line in vcf_contents:
        if not vcf_line:
            continue
        if not vcf_line.startswith("#"):
            vcf_line = vcf_line.split("\t")
            pos = int(vcf_line[1])
            if pos in genome_ends and vcf_line[8] == "seq_end":
                genome_end_line_dic[pos] = "\t".join(vcf_line)
            else:
                try:
                    # merge with seq_end annotations
                    if pos in genome_ends:
                        seen_ends.append(pos)
                    tmp_subs = vcf_line[7].split(",")
                    if "NDM" not in tmp_subs:
                        tmp_subs.insert(0, "NDM")
                    vcf_line[7] = ",".join(tmp_subs)
                    tmp_exc = vcf_line[8].split(",")
                    if "seq_end" not in tmp_exc:
                        tmp_exc.insert(0, "seq_end")
                    vcf_line[8] = ",".join(tmp_exc)

                    # add alt info
                    ref_base, alt_base = pos_info[pos][0], pos_info[pos][1]
                    vcf_line[3] = ref_base
                    vcf_line[4] = alt_base
                except KeyError:
                    print(pos)
                vcf_lines.append("\t".join(vcf_line))
        else:
            vcf_lines.append(vcf_line)

    # fill in genome ends if not already in file
    for i in genome_ends:
        if i not in seen_ends:
            vcf_lines.append(genome_end_line_dic[i])

    # write altered VCF to file, overwriting input
    with open("problematic_sites_sarsCov2.vcf", "w") as out_file:
        fi_content = "\n".join(vcf_lines)
        out_file.write(fi_content)


if __name__ == "__main__":
    main()
