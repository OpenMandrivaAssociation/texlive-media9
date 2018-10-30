Name:		texlive-media9
Version:	0.93
Release:	3
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
%{_texmfdistdir}/tex/latex/media9
%doc %{_texmfdistdir}/doc/latex/media9

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
