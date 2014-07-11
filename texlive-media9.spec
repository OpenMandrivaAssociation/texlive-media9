# revision 33290
# category Package
# catalog-ctan /macros/latex/contrib/media9
# catalog-date 2014-03-25 20:14:30 +0100
# catalog-license lppl1.3
# catalog-version 0.43
Name:		texlive-media9
Version:	0.43
Release:	2
Summary:	Multimedia inclusion package with Adobe Reader-9/X compatibility
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/media9
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/media9.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/media9.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an interface to embed interactive Flash
(SWF) and 3D objects (Adobe U3D & PRC), as well as video and
sound files or streams in the popular MP4, FLV and MP3 formats
into PDF documents with Acrobat-9/X compatibility. Playback of
multimedia files uses the built-in Flash Player of Adobe Reader
and does, therefore, not depend on external plug-ins. Flash
Player supports the efficient H.264 codec for video
compression. The package is based on the RichMedia Annotation,
an Adobe addition to the PDF specification. It replaces the now
obsolete movie15 package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/media9/javascript/3Dmenu.js
%{_texmfdistdir}/tex/latex/media9/javascript/3Dspintool.js
%{_texmfdistdir}/tex/latex/media9/javascript/animation.js
%{_texmfdistdir}/tex/latex/media9/javascript/asylabels.js
%{_texmfdistdir}/tex/latex/media9/media9.sty
%{_texmfdistdir}/tex/latex/media9/players/APlayer.swf
%{_texmfdistdir}/tex/latex/media9/players/APlayer9.swf
%{_texmfdistdir}/tex/latex/media9/players/StrobeMediaPlayback.swf
%{_texmfdistdir}/tex/latex/media9/players/VPlayer.swf
%{_texmfdistdir}/tex/latex/media9/players/VPlayer9.swf
%doc %{_texmfdistdir}/doc/latex/media9/ChangeLog
%doc %{_texmfdistdir}/doc/latex/media9/README
%doc %{_texmfdistdir}/doc/latex/media9/files/3dsystem.fig
%doc %{_texmfdistdir}/doc/latex/media9/files/3dsystem.pdf
%doc %{_texmfdistdir}/doc/latex/media9/files/3dsystem.tex
%doc %{_texmfdistdir}/doc/latex/media9/files/boutona.pdf
%doc %{_texmfdistdir}/doc/latex/media9/files/boutonb.pdf
%doc %{_texmfdistdir}/doc/latex/media9/files/boutonc.pdf
%doc %{_texmfdistdir}/doc/latex/media9/files/boutond.pdf
%doc %{_texmfdistdir}/doc/latex/media9/files/boutone.pdf
%doc %{_texmfdistdir}/doc/latex/media9/files/boutonf.pdf
%doc %{_texmfdistdir}/doc/latex/media9/files/cube.asy
%doc %{_texmfdistdir}/doc/latex/media9/files/cube.mp4
%doc %{_texmfdistdir}/doc/latex/media9/files/cubeposter.png
%doc %{_texmfdistdir}/doc/latex/media9/files/dice.u3d
%doc %{_texmfdistdir}/doc/latex/media9/files/dice.vws
%doc %{_texmfdistdir}/doc/latex/media9/files/dice.wrl
%doc %{_texmfdistdir}/doc/latex/media9/files/epix.asy
%doc %{_texmfdistdir}/doc/latex/media9/files/epix.prc
%doc %{_texmfdistdir}/doc/latex/media9/files/epixposter.pdf
%doc %{_texmfdistdir}/doc/latex/media9/files/mailto.png
%doc %{_texmfdistdir}/doc/latex/media9/files/malte.js
%doc %{_texmfdistdir}/doc/latex/media9/files/malte.u3d
%doc %{_texmfdistdir}/doc/latex/media9/files/players/APlayer.mxml
%doc %{_texmfdistdir}/doc/latex/media9/files/players/APlayer9.mxml
%doc %{_texmfdistdir}/doc/latex/media9/files/players/BSD-License
%doc %{_texmfdistdir}/doc/latex/media9/files/players/SMPfixes.patch
%doc %{_texmfdistdir}/doc/latex/media9/files/players/StrobeMediaPlayback-license
%doc %{_texmfdistdir}/doc/latex/media9/files/players/VPlayer.mxml
%doc %{_texmfdistdir}/doc/latex/media9/files/players/VPlayer9.mxml
%doc %{_texmfdistdir}/doc/latex/media9/files/random.mp4
%doc %{_texmfdistdir}/doc/latex/media9/media9.pdf
%doc %{_texmfdistdir}/doc/latex/media9/media9.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
