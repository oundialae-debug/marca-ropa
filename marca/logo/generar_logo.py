import sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
f=TTFont(sys.argv[1]); out=sys.argv[2]
gs=f.getGlyphSet(); cmap=f.getBestCmap(); upm=f['head'].unitsPerEm
xh=f['OS/2'].sxHeight; hm=f['hmtx']
LS=upm*7/84
def glyph(ch,x):
    g=cmap[ord(ch)]; p=SVGPathPen(gs)
    gs[g].draw(TransformPen(p,(1,0,0,-1,x,0)))  # y flip, baseline y=0
    return p.getCommands(), hm[g][0]
parts=[]; x=0
for ch in 'ne':
    d,a=glyph(ch,x); parts.append(d); x+=a+LS
sw0=upm*.062; w=upm*.36; sx=x; t=-xh; h=xh
X=lambda k:sx+w*k; Y=lambda k:t+h*k
segs=[ # (path, width, opacity): thin top, thick spine, medium fall, tapering breeze
 (f"M{X(.88):.1f} {Y(.14):.1f} C{X(.62):.1f} {Y(-.06):.1f} {X(.04):.1f} {Y(.02):.1f} {X(.14):.1f} {Y(.32):.1f}",sw0*.7,1),
 (f"M{X(.14):.1f} {Y(.32):.1f} C{X(.24):.1f} {Y(.58):.1f} {X(.92):.1f} {Y(.46):.1f} {X(.88):.1f} {Y(.76):.1f}",sw0*1.25,1),
 (f"M{X(.88):.1f} {Y(.76):.1f} C{X(.84):.1f} {Y(1.02):.1f} {X(.42):.1f} {Y(1.0):.1f} {X(.34):.1f} {Y(1.18):.1f} C{X(.28):.1f} {Y(1.34):.1f} {X(.46):.1f} {Y(1.44):.1f} {X(.8):.1f} {Y(1.42):.1f}",sw0*.9,1)]
L=1.9; pts=[(.8,1.42),(.8+(L-.8)*.33,1.39),(.8+(L-.8)*.66,1.41),(L,1.36)]
for i,(wd,op) in enumerate([(.65,1),(.42,.85),(.24,.55)]):
    a,b=pts[i],pts[i+1]; mx=(a[0]+b[0])/2; my=(a[1]+b[1])/2+(-.04 if i%2 else .04)
    segs.append((f"M{X(a[0]):.1f} {Y(a[1]):.1f} Q{X(mx):.1f} {Y(my):.1f} {X(b[0]):.1f} {Y(b[1]):.1f}",sw0*wd,op))
x=sx+w+LS
for ch in 'ma':
    d,a=glyph(ch,x); parts.append(d); x+=a+LS
W=x-LS; top=-f['OS/2'].sCapHeight*0.9; bot=Y(1.6); pad=upm*.12
vb=f"{-pad:.0f} {top-pad:.0f} {W+2*pad:.0f} {bot-top+2*pad:.0f}"
def svg(txt,acc,bg=None):
    s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">'
    if bg: s+=f'<rect x="{-pad:.0f}" y="{top-pad:.0f}" width="{W+2*pad:.0f}" height="{bot-top+2*pad:.0f}" fill="{bg}"/>'
    s+=''.join(f'<path d="{d}" fill="{txt}"/>' for d in parts)
    s+=''.join(f'<path d="{d}" fill="none" stroke="{acc}" stroke-width="{wd:.1f}" stroke-linecap="round"'+(f' opacity="{op}"' if op<1 else '')+'/>' for d,wd,op in segs)
    return s+'</svg>\n'
for name,args in {'logo-color':('#2B2A28','#B4694A'),'logo-ebano':('#2B2A28','#2B2A28'),'logo-crema-fondo-oscuro':('#F7F3EC','#B4694A'),'logo-crema':('#F7F3EC','#F7F3EC')}.items():
    open(f"{out}/{name}.svg",'w').write(svg(*args))
print('ok',vb)
