pkgname=newpasswd
pkgver=0.3
pkgrel=1
pkgdesc="Generate a brand new password"
url="https://github.com/simukis/newpasswd"
license=('ICS')
arch=('any')
depends=('python')
short_hash='57b1305'
source=('https://github.com/simukis/newpasswd/zipball/'$short_hash)
md5sums=('dbbe8e90b3802ec608efe5b086230695')

package() {
    cd $srcdir/simukis-newpasswd-$short_hash/
    mv usr/ $pkgdir/
}
